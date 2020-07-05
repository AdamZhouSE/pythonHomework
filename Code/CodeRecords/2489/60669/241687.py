list=eval(input())
lower=int(input())
upper=int(input())

result=0
for i in range(0,len(list)):
    temp=0
    for j in range(i,len(list)):
        temp+=list[j]
        if lower<=temp<=upper:
            result+=1
print(result)
