# 题目描述
# N 对情侣坐在连续排列的 2N 个座位上，想要牵到对方的手。
# 计算最少交换座位的次数，以便每对情侣可以并肩坐在一起。
# 一次交换可选择任意两人，让他们站起来交换座位。
#
# 人和座位用 0 到 2N-1 的整数表示，情侣们按顺序编号，第一对是 (0, 1)，第二对是 (2, 3)，以此类推，最后一对是 (2N-2, 2N-1)。
#
# 这些情侣的初始座位 row[i] 是由最初始坐在第 i 个座位上的人决定的。

res = 99999
# tot: 0 - 2n-1
def perm(peoples, k, n):
    global res
    if k == 2*n:
        return
    isOK = True
    # print(peoples)
    for i in range(n):
        if abs(peoples[2*i]-peoples[2*i+1]) != 1:
            isOK = False
            break
    if isOK:
        res = min(res, k)
        return

    for i in range(k+1, 2*n):
        peoples[k], peoples[i] = peoples[i], peoples[k]
        perm(peoples, k+1, n)
        peoples[k], peoples[i] = peoples[i], peoples[k]

if __name__ == '__main__':
    li = list(eval(input()))
    perm(li, 0, len(li)//2)
    print(res)