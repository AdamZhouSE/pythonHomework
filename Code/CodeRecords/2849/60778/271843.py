rb=input()
array=list(map(int,input().split()))
array.sort()
res=array[0]
for i in array:
    if(i%res!=0):
        res=-1
        break;
print(res)