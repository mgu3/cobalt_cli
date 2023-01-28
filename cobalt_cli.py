import click

from api import cobalt_api_call_get

TOKEN = "API_Rm/_XZPkTn2Ez|GYFd)Bj}TPinAhnmXzGwVo"


@click.group()
@click.option('--cobalt-api-token', help='Cobalt API Token, can also be set using an environment variable "COBALT_API_TOKEN"')
def cli(cobalt_api_token):
    """ Entry point """
    print("Inside cli")
    print(cobalt_api_token)
    print()
    print()




@cli.command()
def validate_token():
    """ Check that a token is valid """

    status, response = cobalt_api_call_get(TOKEN, "api/cobalt/keycheck/v1.0", None)

    print("Status:", status)
    print("Response:", response)


@cli.command()
def hello(cobalt_api_token):
    """ Print helllo work """
    click.echo("Hello World!!!!!")
    # click.echo(f"--{cobalt_api_token}--")


# @cli.command()
# @click.option('-n', '--name', type=str, help='Name to greet', default='World')
# def hello(name):
#     click.echo(f'Hello {name}')
