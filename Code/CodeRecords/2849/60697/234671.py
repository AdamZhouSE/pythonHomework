size=int(input())
array=list(map(int,input().split(' ')))
for i in range(size):
    res=array[i]
    for j in range(size):
        if(array[j]%array[i]!=0):
            res=-1
            break
    if(res!=-1):
        print(res)
        break
if(res==-1):
    print(res)