n = int(input())
lst = list(map(int,input().split(' ')))

min_paint = min(lst)
if n<min_paint:
    print(-1,end = '')
num = ''
for i in range(n//min_paint-1,-1,-1):#//从最多可以染的数目开始
    for j in range(9,0,-1):
        if n>=lst[j-1] and (n-lst[j-1])//min_paint >= i:
            num+=str(j)
            n-=lst[j-1]
            break
print(num)