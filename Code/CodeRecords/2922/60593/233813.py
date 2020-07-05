n=int(input())
arr=list(map(int,input().split()))
arr=list(set(arr))
if(len(arr)>3):
    print('NO')
else:
    addup=0
    for i in arr:
        addup+=i
    if(addup%len(arr)==0):
        print('YES')
    else:
        print('NO')