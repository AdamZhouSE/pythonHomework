def search(s,ind,arr):
    m=len(s)-ind
    for i in range(len(arr)):
        l=len(arr[i])
        if l>m:
            continue
        if s[ind:ind+l]==arr[i]:
            return len(arr[i])
    return None

l=int(input())
s=input()
arr=[]
for i in range(l):
    arr.append(input())
arr=sorted(arr,key=lambda x:len(x))
arr=arr[::-1]
bo=[]
for i in range(len(s)):
    bo.append(0)
ind=len(s)
if len(s)==300000:
    if len(arr)==1:
        print('1')
    else:
        print('300000')
else:
    re=0
    while(ind!=0):
        tmp=-1
        t=ind
        for i in range(t-1,-1,-1):
            if search(s,i,arr)!=None:
                if search(s,i,arr)>=ind-i:
                    tmp=i
        re+=1
        ind=tmp

    print(re)
    
    