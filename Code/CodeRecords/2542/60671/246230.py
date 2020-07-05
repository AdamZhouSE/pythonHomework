str0=input()
strr1=str0[1:-1]
str1=strr1.split(",")
str1.sort()
numl=[]
for o in str1:
    numl.append(int(o))
numl.sort()
length=len(numl)
count=0
temp=0
for i in range(length-1):
    if(numl[i]+1==numl[i+1]):
        temp+=1
    else:
        if((temp+1)>count):
            count=temp+1
        temp=0
print(count)
        