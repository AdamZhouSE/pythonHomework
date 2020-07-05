t = int(input())
for i in range(t):
    n = int(input())
    a = input().split(" ")
    a = list(map(int, a))
    odd = []
    even = []
    for i in range(n):
        if a[i]%2 ==0:
            even.append(a[i])
        else:
            odd.append(a[i])
    even.extend(odd)
    for i in range(n):
        print(str(even[i])+" ",end="")
    print()