"""
题目描述

n人围成一个圈（从1到n顺时针编号）等待执行。 计数从圆中的点1开始，并沿固定方向（顺时针）围绕圆进行。 在每个步骤中，将跳过一定数量的人，然后执行下一个人。 消灭围绕圈进行（随着被处决者的撤离，圈变得越来越小），直到只有最后一个剩下的人被赋予了自由。 给定总人数n和数字k，表示跳过k-1个人并且第k个人被杀。 任务是选择初始圈子中的位置，以便您成为最后一个幸存者，从而生存下来。 考虑如果n = 5且k = 2，则安全位置为3。首先，杀死位置2的人员，然后杀死位置4的人员，然后杀死位置1的人员。 最终，位置5的人被杀死。 因此，位置3的人幸存下来。

输入描述

输入的第一行包含一个整数T，表示测试用例的数量。然后是T测试用例。每个测试用例的第一行也是唯一一行是由两个以n和k分隔的正整数组成。1 ≤ T ≤ 200；1 ≤ n, k ≤ 200

输出描述

对应于每个测试用例，在新行中打印安全位置。
"""


class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def createLink(n):
    if n <= 0:
        return False
    if n == 1:
        return Node(1)
    else:
        root = Node(1)
        tmp = root
        for i in range(2, n + 1):
            tmp.next = Node(i)
            tmp = tmp.next
        tmp.next = root
        return root


def showLink(root):
    tmp = root
    while True:
        # print(tmp.value)
        tmp = tmp.next
        if tmp == None or tmp == root:
            break


def josephus(n, k):
    if k == 1:
        print( n)
        return
    root = createLink(n)
    tmp = root
    while True:
        for i in range(k - 2):
            tmp = tmp.next
        # print('kill:', tmp.next.value)
        tmp.next = tmp.next.next
        tmp = tmp.next
        if tmp.next == tmp:
            break
    print(tmp.value)


if __name__ == '__main__':
    times = int(input())
    while times > 0:
        times -= 1
        line1 = list(map(int, input().split(" ")))
        josephus(line1[0], line1[1])
