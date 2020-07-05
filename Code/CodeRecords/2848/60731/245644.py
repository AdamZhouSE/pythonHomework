num1,num2=map(int,input().split())
k,m=map(int,input().split())
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
list1.sort()
list2.sort()
res1=list1[0:k]
res2=list2[-m:]
m=max(res1)
n=min(res2)
if m<n:
    print('YES')
else:
    print('NO')