t = int(input())
for i in range(t):
    n = int(input())
    li = [int(x) for x in input().split()]
    even = []
    odd = []
    for i in li:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    even.extend(odd)
    print(*even,end=" \n")