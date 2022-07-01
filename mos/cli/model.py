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

    # List
    lst = subparsers.add_parser('list', help='list models')
    def lst_func(args):
        i = Interface(url=args.url, token=args.token)
        models = i.get_models()
        for m in models:
            print('{} (id={})'.format(m['name'], m['id']))
    lst.set_defaults(func=lst_func)

    # List inputs
    lst_inputs = subparsers.add_parser('list-inputs', help='list model inputs')
    def lst_inputs_func(args):
        m = get_model(get_source, args)
        for f in m.__get_interface_files__(type='input'):
            print('{} (file)'.format(f['name']))
        for o in m.__get_interface_objects__(type='input'):
            print('{} (object)'.format(o['name']))
    lst_inputs.set_defaults(func=lst_inputs_func)

    # List outputs
    lst_outputs = subparsers.add_parser('list-outputs', help='list model outputs')
    def lst_outputs_func(args):
        m = get_model(get_source, args)
        for f in m.__get_interface_files__(type='output'):
            print('{} (file)'.format(f['name']))
        for o in m.__get_interface_objects__(type='output'):
            print('{} (object)'.format(o['name']))
    lst_outputs.set_defaults(func=lst_outputs_func)

    # New
    new = subparsers.add_parser('new', help='create new model from file')
    new.add_argument('model_file', type=str, help='path to model file')
    def new_func(args):
        i = Interface(url=args.url, token=args.token)
        i.new_model(args.model_file, quiet=False)
    new.set_defaults(func=new_func)

    # Delete
    delete = subparsers.add_parser('delete', help='delete model')
    def delete_func(args):
        i = Interface(url=args.url, token=args.token)
        if args.id:
            i.delete_model_with_id(args.id)
        if args.name:
            i.delete_model_with_name(args.name)
    delete.set_defaults(func=delete_func)

    # Get source
    get_source = subparsers.add_parser('get-source', help='get model source code')
    def get_source_func(args):
        m = get_model(get_source, args)
        return m.get_source()
    get_source.set_defaults(func=get_source_func)

    # Get status
    get_status = subparsers.add_parser('get-status', help='get model status')
    def get_status_func(args):
        m = get_model(get_status, args)
        return m.get_status()
    get_status.set_defaults(func=get_status_func)

    return parser


