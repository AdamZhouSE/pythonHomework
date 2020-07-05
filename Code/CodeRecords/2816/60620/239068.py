n=int(input())
a=sorted(list(map(int,input().split())))
result=0
if(len(a)%2==0):
    result=a[len(a)//2-1]
else:
    result=a[(len(a)-1)//2]
print(result)