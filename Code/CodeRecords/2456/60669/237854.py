list=eval(input())
result=[]

for i in range(0,len(list)-1):
    left=list[i]
    num=0
    for j in range(1,len(list)-i):
        right=list[i+j]
        if right<left:
            num+=1
    result.append(num)        
result.append(0)
print(result)