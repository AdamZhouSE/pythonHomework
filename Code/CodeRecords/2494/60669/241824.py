list=eval(input())
result=0

for i in range(0,len(list)-1):
    for j in range(1+i,len(list)):
       if list[i]>2*list[j]:
           result+=1
print(result)