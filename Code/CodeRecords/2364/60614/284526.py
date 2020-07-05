count=0
for i in range(0,int(input())+1):
    temp=str(i)
    for j in temp:
        if temp.count(j)>1:
            count+=1
            break
print(count)