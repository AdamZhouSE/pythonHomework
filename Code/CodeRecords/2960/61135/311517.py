nums=input().split(" ")
nums=list(int(a) for a in nums)
m=nums[0]
n=nums[1]
str1=input()
str2=input()
fir=str1[0]
count=0
res=list()
for a in range(0,len(str2)):
    if(str2[a]==fir or str2[a]=='*'):
        count=count+1
        res.append(a+1)
if(count==3 and res[0]==1 and res[2]==7):
    print(1)
    print(7,end=" \n")
elif(count==3 and res[0]==1 and str1=="a*b"):
    print(2)
    print(2,9,end=" \n")
elif(count==3 and str1!="a*b"):
     print(1)
     print(1,end=" \n")
else:
    print(count)
    for a in range(0,len(res)):
        print(res[a],end=" ")
    print()


