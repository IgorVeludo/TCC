# encoding = utf8
# encoding: iso-8859-1
# encoding: win-1252


class PullRequest:

    def __init__(self, pr_object):
        self.body_pull_request = []
        self.additions = pr_object.additions
        self.assignees = pr_object.assignees
        self.body = pr_object.body
        self.changed_files = pr_object.changed_files # int
        self.closed_at = pr_object.closed_at
        self.comments = pr_object.comments
        self.commits = pr_object.commits
        self.created_at = pr_object.created_at
        self.deletions = pr_object.deletions
        self.diff_url = pr_object.diff_url
        self.id = pr_object.id
        self.issue_url = pr_object.issue_url
        self.labels = pr_object.labels #TODO: analisar classe Label
        self.mergeable = pr_object.mergeable
        self.merged = pr_object.merged
        self.merged_by = pr_object.merged_by #TODO: analisar classe NamedUser
        self.number = pr_object.number
        self.review_comments = pr_object.review_comments
        self.review_comments_url = pr_object.review_comments_url
        self.title = pr_object.title
        self.updated_at = pr_object.updated_at
        self.user = pr_object.user
