import argparse
from mos.interface import Interface

def create_parser(parent):

    # User
    parser = parent.add_parser('user', help='user commands')
    subparsers = parser.add_subparsers(help="sub-command help")

    # Get token
    get_token = subparsers.add_parser('get-token', help='get user token')
    get_token.add_argument('username', type=str)
    get_token.add_argument('password', type=str)
    def get_token_func(args):
        i = Interface(url=args.url, token=args.token)
        return i.get_user_token(args.username, args.password)
    get_token.set_defaults(func=get_token_func)

    return parser