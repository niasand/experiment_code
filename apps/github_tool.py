# -*- coding: utf-8 -*-
# @Time    : 2020-10-06 22:42
# @Author  : Zhiwei Yang
import requests
from secrets import headers, access_token
from github import Github
from urls import *


class GithubIssue():
    def __init__(self):
        self.g = Github(access_token)
        self.repo = self.g.get_repo(my_repo)

    def get_issue_list(self):
        issues = []
        open_issues = self.repo.get_issues()
        for issue in open_issues:
            issues.append(issue)
        return issues

    def create_an_issues(self, title, body):
        self.repo.create_issue(title=title, body=body)

    def get_issue_detail(self):
        ret = self.repo.get_issue(number=issue_number)
        return ret


if __name__ == '__main__':
    G = GithubIssue()
    # print(G.create_an_issues("1", "2"))
    print(G.get_issue_list())
