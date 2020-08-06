# encoding=utf8
# encoding: iso-8859-1
# encoding: win-1252

import click
from github import Github
import sys
from github_api import pull_request
from github_api.repository import get_pr_body
from getpass import getpass

# reload(sys)
# sys.setdefaultencoding('utf8')

@click.command()
def start():
    # """Simple program that greets NAME for a total of COUNT times."""
    # for x in range(count):
    #     click.echo('Hello %s %s' % (repository, name))
    username = input("Digite ser usuario do github: ")
    password = getpass()

    g = Github(username, password)

    pull_requests = get_pr_body(g, 50)

    for item in pull_requests:
        pr = pull_request.PullRequest(item)
        print("numero de commits: " + str(pr.commits))