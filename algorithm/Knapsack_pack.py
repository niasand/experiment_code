# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-09-28 17:40:44
# @Last Modified by:   jerry
# @Last Modified time: 2017-09-28 18:14:35


def pack_result():
    """最简单的背包问题，背包最大容量是10  总共4件物品，价值和重量分别如下
        Knapsack Max weight : weight = 10 (units)
        Total items         : N = 4
        valuesalues of items     : v[] = {10, 40, 30, 50}
        Weight of items     : w[] = {5, 4, 6, 3}

        返回值：拿到的最大价值，和背包的剩余容量
    """

    values = [10, 40, 30, 50]
    weight = [5, 2, 8, 7]
    max_value = 9
    print(get_value(weight, values, max_value, 4))


def get_value(weight, values, max_value, i):
    if i > 1:
        # 不放第i件物品最大价值
        donotputthe_indexi_goods_in_bag_value,\
            donotputthe_indexi_goods_in_bag_weight = get_value(weight, values, max_value, i - 1)
        # 如果第i件物品的重量大于背包最大容量
        if weight[i - 1] > max_value:  # 如果这个地方为真，那就不能放i进去了，因为放i进去，背包就装不下了，既然不放i，那就是返回上面不放i的值，
            return donotputthe_indexi_goods_in_bag_value, donotputthe_indexi_goods_in_bag_weight
        else:  # 如果第i件物品的重量小于背包最大容量，那就可以把i放进去了。那把i放进去了后，包包剩下的重量就是max减去i的重量，
            changed_value, changed_weight = get_value(
                weight, values, max_value - weight[i - 1], i - 1)
            if changed_value + \
                    values[i - 1] > donotputthe_indexi_goods_in_bag_value:
                return changed_value + values[i - 1], changed_weight
            else:
                return donotputthe_indexi_goods_in_bag_value, donotputthe_indexi_goods_in_bag_weight
    else:
        if weight[0] > max_value:
            return 0, max_value
        else:
            return values[0], max_value - weight[0]


if __name__ == '__main__':
    pack_result()
