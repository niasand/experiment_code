# -*- coding: utf-8 -*-
# @Time    : 2020/10/2 21:15
# @Author  : Zhiwei Yang


class CoinChange(object):
    def coin_change(self, coins: list, amount: int) -> int:
        """凑零钱问题：
        给你 k 种⾯值的硬币，⾯值分别为 c1, c2 ... ck ，每种硬
        币的数量⽆限，再给⼀个总⾦额 amount ，问你最少需要⼏枚硬币凑出这个
        ⾦额，如果不可能凑出，算法返回 -1
        coins 中是可选硬币⾯值
        amount 是⽬标⾦额
        """
        dp = [0, 1]
        res = float("INF")
        if amount < 0:
            return -1
        else:
            for coin in coins:
                if amount < coin:
                    return dp[amount]
                else:
                    res = min(dp[amount - coin], res) + 1
                    dp.append(res)
                    print(dp)
        return res


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 2
    c = CoinChange()
    print (c.coin_change(coins, amount))
