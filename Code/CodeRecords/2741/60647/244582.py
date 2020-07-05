list=input()
res=1
for i in range(len(list)):
    length=1
    for j in range(i+1,len(list)-1):
        if list[j]>list[j-1]:
            length+=1
            if length>=res:
                res=length
        else:
            break
print(res)