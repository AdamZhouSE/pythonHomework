from typing import List

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:

    # 记录两个数组中每个数字出现的次数

    result1 = {}

    result2 = {}

    # 遍历两个数组，然后将其数字出现次数添加入字典中

    for i in nums1:

        if i not in result1.keys():

            result1[i] = 1



        else:

            result1[i] += 1

    for i in nums2:

        if i not in result2.keys():

            result2[i] = 1

        else:

            result2[i] += 1

    # 将两个字典的键取出

    k1 = [i for i in result1.keys()]

    k2 = [i for i in result2.keys()]

    # 求两个字典键的交集

    k = set(k1) & set(k2)

    # 结果列表

    r = []

    # 同一个键，代表两个列表中都有出现，然后取最小的值为出现的次数，然后用列表的extend方法添加入结果列表中

    for i in k:
        m = min(result1[i], result2[i])

        r.extend([i] * m)

    return r


if __name__ == "__main__":
    inp1 = input().split("[")
    temp1 = inp1[1].split("]")
    temp2 = temp1[0].split(",")
    for i in range(len(temp2)):
        temp2[i] = int(temp2[i])
    inp2 = input().split("[")
    temp3 = inp2[1].split("]")
    temp4 = temp3[0].split(",")
    for j in range(len(temp4)):
        temp4[j] = int(temp4[j])
    r1 = intersect(temp2, temp4)
    r1.sort()
    print(r1)
