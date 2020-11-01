# -*- coding: utf-8 -*-
# @Time    : 2020-10-06 22:42
# @Author  : Zhiwei Yang
import requests
from github import Github
from apps.secrets import access_token
from apps.urls import my_repo


class GithubIssue():
    def __init__(self):
        self.g = Github(access_token)
        self.repo = self.g.get_repo(my_repo)

    def get_issue_list(self):
        issues = []
        open_issues = self.repo.get_issues()
        for issue in open_issues:
            issues.append(issue.number)
        return issues

    def create_an_issues(self, title, body):
        ret = self.repo.create_issue(title=title, body=body)
        return ret.number

    def get_issue_detail(self, issue_number):
        ret = self.repo.get_issue(number=issue_number)
        msg = "url: {}\ntitle: {}\nbody: {}\n".format(
            ret.url, ret.title, ret.body)
        return msg

    def create_comments(self, issue_number, body):
        issue = self.repo.get_issue(issue_number)
        ret = issue.create_comment(body)
        c = issue.get_comment(ret.id)
        comments = "%s\n%s\n" % (c.html_url, c.body)
        return comments


if __name__ == '__main__':
    G = GithubIssue()
    # issue_number = G.create_an_issues("1", "2")
    # content = G.get_issue_detail(issue_number)
    issue_numbers = G.get_issue_list()
    print(G.create_comments(issue_numbers[0], u"999"))
    # content = G.get_issue_detail(issue_numbers[0])
    # print(content)
