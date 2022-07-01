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
    parser = parent.add_parser('model', help='Model commands')
    parser.add_argument('--name', type=str, help='Model name')
    parser.add_argument('--id', type=str, help='Model ID')
    subparsers = parser.add_subparsers(help="sub-command help")

    # List
    lst = subparsers.add_parser('list', help='List models')
    def lst_func(args):
        i = Interface(url=args.url, token=args.token)
        models = i.get_models()
        for m in models:
            print('{} (id={})'.format(m['name'], m['id']))
    lst.set_defaults(func=lst_func)

    # New
    new = subparsers.add_parser('new', help='Create new model from file')
    new.add_argument('model_file', type=str, help='Path to model file')
    def new_func(args):
        i = Interface(url=args.url, token=args.token)
        i.new_model(args.model_file, quiet=False)
    new.set_defaults(func=new_func)

    # Delete
    delete = subparsers.add_parser('delete', help='Delete model')
    def delete_func(args):
        i = Interface(url=args.url, token=args.token)
        if args.id:
            i.delete_model_with_id(args.id)
        if args.name:
            i.delete_model_with_name(args.name)
    delete.set_defaults(func=delete_func)

    # Get status
    get_status = subparsers.add_parser('get-status', help='Get model status')
    def get_status_func(args):
        m = get_model(get_status, args)
        return m.get_status()
    get_status.set_defaults(func=get_status_func)

    return parser


