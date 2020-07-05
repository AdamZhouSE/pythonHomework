tmp=input().split()
arr=tmp[2]
arr=eval(arr[:len(arr)-1])
k=int(tmp[5][0:1])
t=int(tmp[8])
sign=0
for i in range(k,0,-1):
    for j in range(len(arr)-i):
        if abs(arr[j]-arr[j+i])<=t:
            sign=1
            break
    if sign==1:
        break
if sign==1:
    print('true')
else:
    print('false')