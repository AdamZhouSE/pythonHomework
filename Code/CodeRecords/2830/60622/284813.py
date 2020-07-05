a=list(map(int,input().split()))
k=a[0]
arr=list(map(int,input().split()))
count=0
for i in range(len(arr)):
    count+=pow(k,len(arr)-i -1)
if count%2==0:
    print("even")
else:
    print("odd")
