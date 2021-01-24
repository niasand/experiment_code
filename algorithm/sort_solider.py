# @Author: Zhiwei Yang
# @Date:   2021/1/24


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
    ret = {"len(s)": len(s), "len(s) * n":  len(s) * n}
    return ret
