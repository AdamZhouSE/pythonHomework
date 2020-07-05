n=int(input())
num=input().split()
for i in range(n):
    num[i]=int(num[i])
num=list(set(num))
result=len(num)
if 0 in num:
    result-=1
print(result)