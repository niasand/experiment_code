# @Author: jerry
# @Date:   2018-03-04T23:04:16+08:00
# @Last modified by:   jerry
# @Last modified time: 2018-03-05T23:09:57+08:00

from urllib import request
import morse_talk as mtalk
from bs4 import BeautifulSoup
from requests_toolbelt import MultipartEncoder
import requests
from itertools import product, combinations


def get0():
    m = MultipartEncoder(
        fields={
            'field0': 'value',
            'field1': 'value',
            'field2': (
                'filename',
                open(
                    '/Users/yang/Desktop/Screen Shot 2018-04-02 at 3.20.23 PM.png',
                    'rb'),
                'text/plain')})

    r = requests.post('http://httpbin.org/post', data=m,
                      headers={'Content-Type': m.content_type})
    print(r.status_code)


def get_pic():
    url = "https://detail.1688.com/offer/560514443414.html"
    html = request.urlopen(url)
    soup = BeautifulSoup(html, "lxml")
    i = 0
    for link in soup.find_all('img'):
        i += 1
        imgurl = link.get("src")
        if not imgurl.startswith("http"):
            pass
        else:
            print(imgurl)
            request.urlretrieve(imgurl, "log/%02d.jpg" % i)


def mos_conten():
    content = 'i love you'
    mo_content = mtalk.encode(content)
    print(mo_content)


def _p():

    a = [1]
    b = [2, 3]
    c = [4, 5]
    for x, y, z in product(a, b, c):
        print(x, y, z)


def bucket_sort(soliders):
    max_height = max(soliders)
    buckets = [0] * (max_height + 1)
    for i in soliders:
        buckets[i] += 1
    sorted_nums = []
    print("buckets", buckets)
    for j in range(len(buckets)):
        if buckets[j] != 0:
            for y in range(buckets[j]):
                sorted_nums.append(j)
    return sorted_nums


def random_pick(sorted_soliders, n, max_height_minus=2):
    s = []
    print("sorted_soliders", sorted_soliders)
    if len(sorted_soliders) <= n:
        if (max(sorted_soliders) - min(sorted_soliders)) > max_height_minus:
            print("first not found soliders")
            return 0
        return sorted_soliders
    grouped = []
    for i in range(0, len(sorted_soliders), n):
        b = sorted_soliders[i: i + n]
        if len(b) == n and len(b) >= 2:
            print("b", b)
            grouped.append(b)
    print("grouped", grouped)
    for j in grouped:
        if (max(j) - min(j)) > max_height_minus:
            continue
        s.append(j)
    print("s", s)
    d = {"len(s)": len(s), "len(s) * n":  len(s) * n}
    return d


if __name__ == '__main__':
    # print (recursion(8))
    # _p()
    k_rows = 2
    max_height_minus = 3
    soliders = [1, 2, 2, 2, 10]
    sorted_soliders = bucket_sort(soliders)
    n = len(soliders)
    for i in range(1, n + 1):
        d = random_pick(sorted_soliders, i)
        print(d)
