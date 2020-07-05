n = int(input())
list1 = list(map(int,input().split()))
list1.sort()
result = 0
for i in range(n-1,-1,-1):
    result += list1[i]
    if result%2==0:
        print(result)
        break