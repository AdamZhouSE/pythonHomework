a=int(input())
b=input()
list=[]
for i in range(0,len(b)):
    list.append(int(b[i]))
result=0
for i in range(0,len(list)):
    result=result*10
    result=result+a*list[i]
print(result)