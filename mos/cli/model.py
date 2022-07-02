import json
import tempfile
import argparse
from mos.interface import Interface

def get_model(parser, args):
    i = Interface(url=args.url, token=args.token)
    if args.id:
        m = i.get_model_with_id(args.id)
    elif args.name:
        m = i.get_model_with_name(args.name)
    else:
        parser.error("model id or name must be provided")
    return m

def create_parser(parent):

    # Model
    parser = parent.add_parser('model', help='model commands')
    parser.add_argument('--name', type=str, help='model name')
    parser.add_argument('--id', type=str, help='model id')
    subparsers = parser.add_subparsers(help="sub-command help")

    # Delete
    delete = subparsers.add_parser('delete', help='delete model')
    def delete_func(args):
        i = Interface(url=args.url, token=args.token)
        if args.id:
            i.delete_model_with_id(args.id)
        if args.name:
            i.delete_model_with_name(args.name)
    delete.set_defaults(func=delete_func)

    # Get execution log
    get_exec_log = subparsers.add_parser('get-execution-log', help='get model run execution log')
    def get_exec_log_func(args):
        m = get_model(parser, args)
        return m.get_execution_log()
    get_exec_log.set_defaults(func=get_exec_log_func)

    # Get source
    get_source = subparsers.add_parser('get-source', help='get model source code')
    def get_source_func(args):
        m = get_model(parser, args)
        return m.get_source()
    get_source.set_defaults(func=get_source_func)

    # Get status
    get_status = subparsers.add_parser('get-status', help='get model status')
    def get_status_func(args):
        m = get_model(parser, args)
        return m.get_status()
    get_status.set_defaults(func=get_status_func)

    # Get variable state
    get_var_state = subparsers.add_parser('get-variable-state', help='get variable state')
    get_var_state.add_argument('var_name', type=str, help='variable name')
    def get_var_state_func(args):
        m = get_model(parser, args)
        state = m.get_variable_state(args.var_name, field='all', typed=False)
        keys = ['index', 'label', 'kind', 'value', 'lower_bound', 'upper_bound']
        print(', '.join(keys))
        for s in state:
            print('{}, {}, {}, {:.5e}, {:.5e}, {:.5e}'.format(
                *[s[key] for key in keys]
            ))
    get_var_state.set_defaults(func=get_var_state_func)

    # Get function state
    get_func_state = subparsers.add_parser('get-function-state', help='get function state')
    get_func_state.add_argument('func_name', type=str, help='function name')
    def get_func_state_func(args):
        m = get_model(parser, args)
        state = m.get_function_state(args.func_name, field='all', typed=False)
        keys = ['index', 'label', 'value']
        print(', '.join(keys))
        for s in state:
            print('{}, {}, {:.5e}'.format(
                *[s[key] for key in keys]
            ))
    get_func_state.set_defaults(func=get_func_state_func)

    # Get constraint state
    get_constr_state = subparsers.add_parser('get-constraint-state', help='get constraint state')
    get_constr_state.add_argument('constr_name', type=str, help='constraint name')
    def get_constr_state_func(args):
        m = get_model(parser, args)
        state = m.get_constraint_state(args.constr_name, field='all', typed=False)
        keys = ['index', 'label', 'kind', 'dual', 'violation']
        print(', '.join(keys))
        for s in state:
            print('{}, {}, {}, {:.5e}, {:.5e}'.format(
                *[s[key] for key in keys]
            ))
    get_constr_state.set_defaults(func=get_constr_state_func)

    # Get interface file
    get_int_file = subparsers.add_parser('get-interface-file', help='get interface file')
    get_int_file.add_argument('file_name', type=str, help='name of interface file')
    def get_int_file_func(args):
        m = get_model(parser, args)
        f = tempfile.NamedTemporaryFile(delete=True)
        m.get_interface_file(args.file_name, filepath=f.name)
        print(f.read().decode('utf-8'))
        f.close()
    get_int_file.set_defaults(func=get_int_file_func)

    # Get interface object
    get_int_obj = subparsers.add_parser('get-interface-object', help='get interface object')
    get_int_obj.add_argument('obj_name', type=str, help='name of interface object')
    def get_int_obj_func(args):
        m = get_model(parser, args)
        o = m.get_interface_object(args.obj_name)
        print(json.dumps(o, indent=4))
    get_int_obj.set_defaults(func=get_int_obj_func)

    # List
    lst = subparsers.add_parser('list', help='list models')
    def lst_func(args):
        i = Interface(url=args.url, token=args.token)
        models = i.get_models()
        for m in models:
            print('{} (id={})'.format(m['name'], m['id']))
    lst.set_defaults(func=lst_func)

    # List components
    lst_components = subparsers.add_parser('list-components', help='list all model components')
    def lst_comp_func(args):
        m = get_model(parser, args)
        m.show_components()
    lst_components.set_defaults(func=lst_comp_func)

    # List inputs
    lst_inputs = subparsers.add_parser('list-inputs', help='list model inputs')
    def lst_inputs_func(args):
        m = get_model(parser, args)
        for f in m.__get_interface_files__(type='input'):
            print('{} (file)'.format(f['name']))
        for o in m.__get_interface_objects__(type='input'):
            print('{} (object)'.format(o['name']))
    lst_inputs.set_defaults(func=lst_inputs_func)

    # List outputs
    lst_outputs = subparsers.add_parser('list-outputs', help='list model outputs')
    def lst_outputs_func(args):
        m = get_model(parser, args)
        for f in m.__get_interface_files__(type='output'):
            print('{} (file)'.format(f['name']))
        for o in m.__get_interface_objects__(type='output'):
            print('{} (object)'.format(o['name']))
    lst_outputs.set_defaults(func=lst_outputs_func)

    # List variables
    lst_variables = subparsers.add_parser('list-variables', help='list model variables')
    def lst_variables_func(args):
        m = get_model(parser, args)
        for v in m.__get_variables__():
            print(v['name'])
    lst_variables.set_defaults(func=lst_variables_func)

    # List functions
    lst_functions = subparsers.add_parser('list-functions', help='list model functions')
    def lst_functions_func(args):
        m = get_model(parser, args)
        for f in m.__get_functions__():
            print(f['name'])
    lst_functions.set_defaults(func=lst_functions_func)

    # List constraints
    lst_constraints = subparsers.add_parser('list-constraints', help='list model constraints')
    def lst_constraints_func(args):
        m = get_model(parser, args)
        for c in m.__get_constraints__():
            print(c['name'])
    lst_constraints.set_defaults(func=lst_constraints_func)

    # New
    new = subparsers.add_parser('new', help='create new model from file')
    new.add_argument('model_file_path', type=str, help='path to model file')
    def new_func(args):
        i = Interface(url=args.url, token=args.token)
        i.new_model(args.model_file, quiet=False)
    new.set_defaults(func=new_func)

    # Run
    run = subparsers.add_parser('run', help='run model')
    run.add_argument('--non-blocking', action='store_true', help='model run without blocking command execution')
    run.add_argument('--poll_time', type=int, default=1, help='polling time in seconds when blocking')
    def run_func(args):
        m = get_model(parser, args)
        m.run(blocking=not args.non_blocking, poll_time=args.poll_time)
    run.set_defaults(func=run_func)

    # Set interface file
    set_int_file = subparsers.add_parser('set-interface-file', help='set model interface file')
    set_int_file.add_argument('file_name', type=str, help='name of interface file')
    set_int_file.add_argument('file_path', type=str, help='path to interface file')
    def set_int_file_func(args):
        m = get_model(parser, args)
        m.set_interface_file(args.file_name, args.file_path)
    set_int_file.set_defaults(func=set_int_file_func)

    # Set interface object
    set_int_obj = subparsers.add_parser('set-interface-object', help='set model interface object')
    set_int_obj.add_argument('obj_name', type=str, help='name of interface object')
    set_int_obj.add_argument('obj_data', type=str, help='interface object data')
    def set_int_obj_func(args):
        m = get_model(parser, args)
        m.set_interface_object(args.obj_name, json.loads(args.obj_data))
    set_int_obj.set_defaults(func=set_int_obj_func)

    # Parser ready
    return parser


