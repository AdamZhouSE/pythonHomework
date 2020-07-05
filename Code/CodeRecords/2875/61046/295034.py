num=int(input())
test=input().split()
all=[]
res=[]

for i in range(num):
    temp=[]
    temp.append(str(i+1))
    temp.append(test[i])
    all.append(temp)

count=dict(all)
newc=sorted(count.items(),key=lambda item:item[1])
for key,value in newc:
    res.append(key)
    
print(str(" ".join(res)))
