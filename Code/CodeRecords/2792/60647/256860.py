n=input()
list=input().split()
count=1
num=1
res=[]
for i in range(len(list)):
    if i !=len(list)-1:
        if list[i]>=list[i+1]:
            res.append(count)
            count=1
            num+=1
        else:
            count+=1
    else:
        if list[i-1]>=list[i]:
            count=1
            
        res.append(count)
print(num)
for i in range(len(res)-1):
    print(res[i],end=" ")
print(res[len(res)-1])