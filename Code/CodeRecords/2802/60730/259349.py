num, m = map(int, input().split())
n = list(map(int, input().split()))
for i in range(num):
    if n[i] % m != 0:
        n[i] = int(n[i] / m) + 1
    else:
        n[i] = int(n[i] / m)
numlist = list(set(n))
if numlist == [1]:
    print(num)
else:
    n.reverse()
    print(num-n.index(max(n)))  # 打印出索引的第一个元素，所以最后要num减去
