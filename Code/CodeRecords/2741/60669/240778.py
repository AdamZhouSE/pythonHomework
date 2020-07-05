list=eval(input())
result=0
temp=1
for i in range(0,len(list)-1):
    if list[i]<list[i+1]:
        temp+=1
    else:
        if temp>result:
            result=temp
print(result)