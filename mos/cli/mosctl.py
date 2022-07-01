import argparse
from . import user
from . import model

def create_parser():

    parser = argparse.ArgumentParser(prog='mosctl')

    parser.add_argument('--url', type=str, help='backend url (defaults to using env vars MOS_BACKEND_HOST and MOS_BACKEND_PORT)')
    parser.add_argument('--token', type=str, help='user token (defaults to using env var MOS_BACKEND_TOKEN')
    parser.set_defaults(func=lambda args: None)

    # Subcommands
    subparsers = parser.add_subparsers(help="sub-command help")
    user.create_parser(subparsers)
    model.create_parser(subparsers)  

    return parser
 
def main():
    mosctl = create_parser()
    args = mosctl.parse_args()
    return args.func(args)
    
if __name__ == "__main__":
    r = main()
    if r is not None:
        print(r)

