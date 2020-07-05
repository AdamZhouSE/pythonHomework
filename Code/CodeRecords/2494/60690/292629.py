list=input()[1:-1].split(",")
for i in range(len(list)):list[i]=int(list[i])
res=0
for i in range(len(list)-1):
    for j in range(i+1,len(list)):
        if list[i]>2*list[j]:
            res+=1
print(res)