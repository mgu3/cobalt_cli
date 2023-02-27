"""
Main entry point for the cobalt_cli

We looked at using click for this, but seemed to be harder than just using the built-in argparse

setup.py points the cli to here.

"""

import argparse
import getpass
import os
from dataclasses import dataclass

from keys.keys import keys
from notifications.notifications import notifications


@dataclass()
class GlobalValues:
    cobalt_api_key: str
    cobalt_environment: str


def option_is(args, check_for):
    """ Helper to see if a value exists in the args """

    return bool(check_for in args and args[check_for])


def create_menu(top_parser_sub_parsers):
    """ rather repetitive code to create the command menu """

    # key menu
    parser_key = top_parser_sub_parsers.add_parser('key', help='Api key commands')
    # parser_key.add_argument('--bar', type=int, help='bar is useful option')
    parser_key.set_defaults(key=True)

    # key sub menu
    key_sub_parsers = parser_key.add_subparsers()
    parser_key_list = key_sub_parsers.add_parser('list', help='List your keys')
    parser_key_list.set_defaults(key_list=True)
    parser_key_add = key_sub_parsers.add_parser('add', help='Add a new key')
    parser_key_add.set_defaults(key_add=True)

    # notification menu
    parser_notifications = top_parser_sub_parsers.add_parser('notifications', help='Notification commands')
    # parser_notifications.add_argument('--foo', type=int, help='foo is useful option')
    parser_notifications.set_defaults(notifications=True)

    # notifications sub menu
    notifications_sub_parsers = parser_notifications.add_subparsers()
    parser_notifications_file_upload = notifications_sub_parsers.add_parser('file_upload',
                                                                            help='Upload a file with messages to send')
    parser_notifications_file_upload.set_defaults(notifications_file_upload=True)


def cli():
    """ Entry point """
    # create the top-level parser
    top_parser = argparse.ArgumentParser(description="Command line interface for the Cobalt API", epilog="You can also set environment variables COBALT_API_KEY and COBALT_ENVIRONMENT if you don't want to pass them as parameters.")

    # Arguments for every option
    top_parser.add_argument('--cobalt-api-key', default=os.environ.get('COBALT_API_KEY'),
                            help='api key, set up with the key options')
    cobalt_environment_from_variables = os.environ.get('COBALT_ENVIRONMENT', 'PRODUCTION')
    top_parser.add_argument('--cobalt-environment', default=cobalt_environment_from_variables,
                            help='For Development. Allows commands to be run against test environments.')

    # create sub-parser for command menu, then add the menus
    top_parser_sub_parsers = top_parser.add_subparsers(help='sub-command help')

    # Add the command menu and sub menu options
    create_menu(top_parser_sub_parsers)

    # Get the arguments
    args = vars(top_parser.parse_args())
    print(args)

    # handle globals - parameters that we use for everything
    global_values = GlobalValues(cobalt_api_key=args.get("cobalt-api-key"),
                                 cobalt_environment=args.get("cobalt-environment"))

    # Direct the call to the right top level command, they can handle the rest
    if option_is(args, "key"):
        return keys(args, global_values)

    elif option_is(args, "notifications"):
        return notifications(args, global_values)

    # If we get here show the help message
    top_parser.print_help()
