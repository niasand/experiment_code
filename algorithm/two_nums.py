# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-09-25 21:40:27
# @Last Modified by:   jerry
# @Last Modified time: 2017-09-25 21:45:54
import typer

app = typer.Typer()


class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twosum(self, numbers, target):
        ret = []
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    ret.append(i)
                    ret.append(j)

        return ret


class Solution1(object):
    def twosum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i, m in enumerate(nums):
            if m not in d:
                d[m] = i
            ret = target - nums[i]
            if ret in d.keys() and ret != i:
                print(d)
                return [ret, i]
            # else:
            #     print ("no solutions")


def soluton1():
    nums = [2, 7, 11, 15]
    target = 9
    r = Solution1()
    s = r.twosum(nums, target)
    print(s)


def solution():
    a = Solution()
    numbers = [98, 23, 3, 4, 5]
    target = 26
    c = a.twosum(numbers, target)


def main(name: str):
    typer.echo(f"Hello {name}")


@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")


if __name__ == '__main__':
    # soluton1()
    # solution()
    # typer.run(main)
    app()
