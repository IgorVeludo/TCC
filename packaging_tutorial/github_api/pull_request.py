# encoding = utf8
# encoding: iso-8859-1
# encoding: win-1252


class PullRequest:

    def __init__(self):
        self.body_pull_request = []

    def get_pr_body(self, github_auth, nu_stars):

        repositories = github_auth.search_repositories(query='language:python')
        stars_repo = []

        for r in repositories:
            if(r.stargazers_count >= nu_stars):
                stars_repo.append(r)
                # print(r.stargazers_count)
                break

        pull_request = stars_repo[0].get_pulls(
            state='closed', sort='created', base='master')

        for item in pull_request:
            self.body_pull_request.append(item)

        for item in self.body_pull_request:
            print(item.body)
            # print(item.get_issue_comments)

        # self.save_data()

    def save_data(self):
        with open('comments.json', 'w') as write:
            write.write(str(self.body_pull_request))
        # print(type(pull_request))
        # print(pull_request)
