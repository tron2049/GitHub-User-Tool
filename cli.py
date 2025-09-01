import argparse


def user_activity():  #Handles user input
    parser = argparse.ArgumentParser(description='GitHub activity tracker CLI command tool')
    subparser = parser.add_subparsers(description='Command line arguments',dest='command', required=True)
    
    user_parser = subparser.add_parser('username', help='Username input')
    user_parser.add_argument('name', help='name of the user')
    
    args = parser.parse_args()
    
    return args

