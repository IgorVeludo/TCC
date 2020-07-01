# encoding=utf8
# encoding: iso-8859-1 
# encoding: win-1252

import click
from github import Github
import sys
reload(sys)
sys.setdefaultencoding('utf8')

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

    # open_issues = repo.get_issues(state='open')
    # for issue in open_issues:
    #     print(issue)

    ## Get count of stars
    # print("Quantidade de estrelas: {}".format(repo.stargazers_count))

    ## Search repository by language
    # repositories = g.search_repositories(query='language:python')
    # for repo in repositories:
    #     print(repo)
    commits = repo.get_commits()
    
    for commit in commits:     
        print(commit.commit.author)

