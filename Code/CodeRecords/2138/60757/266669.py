def calarr(arr):
    count=0
    for i in range(len(arr)):
        count=count+arr[i]
    return count
arr=list(eval(input()))
k=int(input())
sign=0
for i in range(2,len(arr)+1):
    for j in range(len(arr)+1-i):
        li=arr[j:j+i]
        if calarr(li)%k==0:
            sign=1
            break
    if sign==1:
        break
if sign==1:
    print(True)
else:
    print(False)
            