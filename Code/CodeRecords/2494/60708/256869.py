list=eval(input())
result=0
for i in range(0,len(list)-1):
    for j in range(i+1,len(list)):
        if list[i]>2*list[j]:
            result=result+1
print(result)