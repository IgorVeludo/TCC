# encoding=utf8
# encoding: iso-8859-1
# encoding: win-1252

import click
from github import Github
import sys
from github_api import pull_request

# reload(sys)
# sys.setdefaultencoding('utf8')


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

    g = Github(username, password)

    pr = pull_request.PullRequest()
    pr.get_pr_body(g, 50)
