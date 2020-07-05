def func(str1):
    if(str1=="A"):
        return 4.0
    elif(str1=="B"):
        return 3.0
    elif(str1=="C"):
        return 2.0
    elif(str1=="D"):
        return 1.0
    else:
        return 0.0

n=int(input())
sum1=0
str1=input()
for i in range(0,n):
    sum1=sum1+func(str1[i])
if(sum1==0):
    print(0,end="")
else:
    print("%.14f"%(sum1/n),end="")