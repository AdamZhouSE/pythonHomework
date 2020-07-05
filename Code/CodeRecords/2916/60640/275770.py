"""
在数组中寻找4,8,15,16,23,42 的序列
用六位的数组存储每个数的数量，
遇到一个数，如果该数数量为0，则它的数量加1
如果该数数量不为0，但它的前一个数数量>0,则前一个数数量-1，它的数量加一
相当于前一个被该序列消耗掉了，最后一位42上如果是1，就表示有一个这样的序列
"""
n = int(input())
inp = [int(x) for x in input().split(" ")]
dic = {4: 0, 8: 1, 15: 2, 16: 3, 23: 4, 42: 5}
count = [0, 0, 0, 0, 0, 0]
for num in inp:
    pos = dic[num]
    # 如果是4
    if pos == 0:
        count[pos] += 1
    elif count[pos-1] > 0:
        count[pos-1] -= 1
        count[pos] += 1
res = n-6*count[5]
print(res)
