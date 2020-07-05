import sys

def checkOk(lst,cap,D):
    count=0
    i=0
    while i<len(lst):
        j=i
        sum=0
        while j<len(lst) and sum+lst[j]<=cap:
            sum+=lst[j]
            j+=1
        count+=1
        if count>D:
            return False
        i=j
    return True

lst=eval((input()))
NUM=int(input())

if NUM==len(lst):
    print(max(lst),end="")
else:
    left =sys.maxsize
    right=0
    for i in  lst:
        left=min(i,left)
        right+=i

    while left<right:
        cap=left+(right-left)//2
        if checkOk(lst,cap,NUM):
            right=cap
        else:
            left=cap+1
    print(left)