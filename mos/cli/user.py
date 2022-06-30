import argparse

def create_parser(parent):

    # User
    parser = parent.add_parser('user', help='User commands')
    subparsers = parser.add_subparsers(help="sub-command help")

    return parser