abc=input()
a=len(abc)
array=list(map(int,abc[1:a-1].split(',')))
res={}
for i in array:
    if(i in res.keys()):
        res[i]=res[i]+1
    else:
        res[i]=1
res=sorted(res.items(),key=lambda x:x[1],reverse=True)
even=0
l=len(array)
tmp=0
j=0
arr=[0 for i in range(l)]
while even<l:
    if(res[j][1]>tmp):
        arr[even]=res[j][0]
        tmp=tmp+1
    else:
        j=j+1
        arr[even] = res[j][0]
        tmp=1
    even=even+2
even=1
while even<l:
    if(res[j][1]>tmp):
        arr[even]=res[j][0]
        tmp=tmp+1
    else:
        j=j+1
        arr[even] = res[j][0]
        tmp = 1
    even=even+2
print(arr)
