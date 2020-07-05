nums = int(input())
res = []
for i in range(nums):
    length = int(input())
    list1 = input().split(" ")
    even = []
    odd = []
    for j in list1:
        if int(j) % 2 == 0:
            even.append(j)
        elif int(j) % 2 != 0:
            odd.append(j)
    even.sort()
    odd.sort()
    odd.reverse()
    res.append(" ".join(odd + even))
for i in res:
    print(i)