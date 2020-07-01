import click
from github import Github


@click.command()
@click.option('--repository',
              help='insira a url do repositorio que deseja ser analisado.')
@click.option('--username',
              help='Type your username')
@click.option('--password',
              help='Type your password')
def start(repository, username, password):
    # """Simple program that greets NAME for a total of COUNT times."""
    # for x in range(count):
    #     click.echo('Hello %s %s' % (repository, name))

    # github_api.getRepository(username, password)

    g = Github(username, password)

    repo = g.get_repo(repository)

    open_issues = repo.get_issues(state='open')
    for issue in open_issues:
        print(issue)
