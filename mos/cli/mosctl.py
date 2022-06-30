import argparse
import user 
import model 

def create_parser():

    parser = argparse.ArgumentParser(prog='mosctl')

    parser.add_argument('--url', type=str, help='Backend URL')
    parser.add_argument('--token', type=str, help='User token')
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
    print(main())

