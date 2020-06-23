import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--repository',
              help='insira a url do repositorio que deseja ser analisado.')
def start(count, repository):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % repository)
