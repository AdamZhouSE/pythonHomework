num = list(map(int,input().split(',')))
k = int(input())
num.sort()
print(num[len(num)-k])