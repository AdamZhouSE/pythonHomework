num = int(input())
for j in range(num):
    n = int(input())
    arr = list(map(int,input().split()))
    odd = []
    even = []
    for i in arr:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    for i in even+odd:
        print(i,end=" ")
    print()