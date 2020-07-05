n=input()
n=n[1:len(n)-1]
list=n.split(',')
res=len(list)
for i in range(0,len(list)-1):
    if(list[i]>list[i+1]):
        res=res-1
print(res)