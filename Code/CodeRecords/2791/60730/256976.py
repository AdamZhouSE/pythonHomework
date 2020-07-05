m = int(input())
n = list(map(int, input().split()))
num = n.count(1)
print(num)
tmp = 1
num_list = []
for i in range(1, len(n)):
    if (i == len(n) - 1):
        num_list.append(tmp)
    if (n[i] != 1):
        tmp = tmp + 1
    else:
        num_list.append(tmp)
        tmp = 1
print(" ".join(map(str, num_list)))
