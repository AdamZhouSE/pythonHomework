n=int(input())
arr=list(map(int,input().split()))
addup=0
for i in arr:
    addup+=i
if(addup%n!=0):
    print('NO')
else:
    avg=int(addup/n)
    arr.sort()
    ans='YES'
    for i in range(len(arr)):
        if(arr[n-1-i]+arr[i]!=avg*2):
            ans='NO'
    print(ans)