arr=eval(input())
k=int(input())
re=1
flag=False
while re<=len(arr):
    for i in range(0,len(arr)+1-re):
        temp=0
        for j in range(i,i+re):
            temp+=arr[j]
        if temp>=k:
            flag=True
            break
    if flag:
        break
    re+=1
if flag:
    print(re)
else:
    print(-1)