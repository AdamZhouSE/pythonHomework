s=input()
#print(s)
str=s[1:len(s)-1]
l=str.split(",")
for i in range(len(l)):
    l[i]=int(l[i])
sum=0
for i in range(len(l)-1):
    for j in range(1,len(l),1):
        if l[i]>2*l[j]:
            sum=sum+1
print(sum)