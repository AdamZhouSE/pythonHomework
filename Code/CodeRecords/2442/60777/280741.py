temp=input()
temp=temp[1:len(temp)-1]
get=[int(x) for x in temp.split(',')]

get.sort()
res=0
for i in range(len(get)-1):
    if((get[i+1]-get[i])>res):
        res=get[i+1]-get[i]
print(res)