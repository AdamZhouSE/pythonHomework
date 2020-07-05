len=int(input())
strList=input().split()
array=[]
for c in strList:
    array.append(int(c))
res=-1
array.sort()
check = 1
for k in range(1,len):
    if array[k]%array[0]!=0:
        check=0
        break
if check==1:
    res=array[0]    
print(res)

