num=int(input())
lst=[]
for i in range(num):
    temp=input().split(',')
    temp=list(map(int,temp))
    lst.append(temp)
n=int(input())
res = [0] * n
for i, j, k in lst:
    for l in range(i-1, j):
        res[l] += k
print(res)