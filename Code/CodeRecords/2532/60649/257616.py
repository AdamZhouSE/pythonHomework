arr=eval(input())
lens=len(arr)
arr2=sorted(arr)
pos=0
res=0
tmpmax=0
while pos<lens:
    tmpmax=max(arr[pos],tmpmax)
    if tmpmax==arr2[pos]:
        res+=1
    pos+=1
print(res)