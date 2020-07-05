str1=input()
str2=input()
str1=str1.split(" ")
str2=str2.split(" ")
num=int(str1[0])
time=int(str1[1])
for i in range(0,len(str2)):
    str2[i]=int(str2[i])
str2.sort()
sig=1
if(time==1):
    sig=0
cost=0
for i in range(0,len(str2)):
    cost+=str2[i]*time
    if(sig==1):
        time=time-1
        if(time==1):
            sig=0
print(cost)
