import click


# @click.command()
# def cli():
#     """Example script."""
#     click.echo('Hello World!')


@click.group()
def cli():
    pass


@cli.command()
def hello():
    """ Print helllo work """
    click.echo("Hello World")


@cli.command()
@click.option('-n', '--name', type=str, help='Name to greet', default='World')
def hello(name):
    click.echo(f'Hello {name}')
