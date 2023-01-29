import click

from api import cobalt_api_call_get

# TOKEN=API_Rm/_XZPkTn2Ez|GYFd)Bj}TPinAhnmXzGwVo


# @click.group()
# def cli():
#     pass
#
#
# @click.command()
# @click.option('--username', envvar='USERNAME')
# def greet(username):
#     click.echo(f"Hello {username}!")

@click.group()
# @click.option('--token', envvar='TOKEN')
# @click.option('--cobalt-api-token', envvar='COBALT', help='Cobalt API Token, can also be set using an environment variable "COBALT_API_TOKEN"')
def cli():
    """ Entry point """
    print("Inside cli")
    # print(token)
    print()
    print()


@cli.command()
@click.option('--cobalt-api-token', envvar='COBALT_API_TOKEN')
def validate_token(cobalt_api_token):
    """ Check that a token is valid """

    print("TOKEN:", cobalt_api_token)

    status, response = cobalt_api_call_get(cobalt_api_token, "api/cobalt/keycheck/v1.0", None)

    print("Status:", status)
    print("Response:", response)


@cli.command()
@click.option('--cobalt-api-token', envvar='COBALT')
def hello(cobalt_api_token):
    """ Print helllo work """
    click.echo("Hello World!!!!!")
    # click.echo(f"--{cobalt_api_token}--")


# @cli.command()
# @click.option('-n', '--name', type=str, help='Name to greet', default='World')
# def hello(name):
#     click.echo(f'Hello {name}')
