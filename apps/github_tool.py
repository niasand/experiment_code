# -*- coding: utf-8 -*-
# @Time    : 2020-10-06 22:42
# @Author  : Zhiwei Yang
import requests
from secrets import headers
from urls import *


class GithubIssue():
    def __init__(self):
        self.g = requests.Session()

    def get_issue_list(self):
        r = self.g.get(github_base_url + issues_url, headers=headers)
        if r.status_code == 200:
            return r.json()
        else:
            return {"retcode": -1}

    def create_an_issues(self, title, body):
        data = {"title": title, "body": body}
        r = self.g.post(github_base_url + issues_url, json=data, headers=headers)
        if r.status_code == 200:
            return r.json()
        else:
            return {"retcode": -1}

    def get_issue_detail(self, issue_number):
        issue_detail = "{}/{}".format(issues_url, issue_number, headers=headers)
        r = self.g.get(github_base_url + issue_detail)
        if r.status_code == 200:
            return r.json()
        else:
            return {"retcode": -1}


if __name__ == '__main__':
    G = GithubIssue()
    # print(G.create_an_issues("1", "2"))
    print(G.get_issue_list())
