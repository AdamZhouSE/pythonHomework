num=input().replace("[","").replace("]","").split(",")
for i in range(len(num)):
    for j in range(i,len(num)):
        if num[i]>num[j]:
            temp=num[i]
            num[i]=num[j]
            num[j]=temp

print("[",end="")
for i in range(len(num)):
    if(i!=len(num)-1):
        print(num[i],end=", ")
    else:
        print(num[i],end="")
print("]")