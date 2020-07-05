
n=int(input())
m=int(input())
list1=[]
for i in range(n,m+1):
    str1=str(i)
    flag=True
    for j in range(0,len(str1)):
        if str1[j]=="0":
            flag=False
        elif (i%int(str1[j]))!=0:
                flag=False
    if(flag):
        list1.append(i)
print(list1)
            