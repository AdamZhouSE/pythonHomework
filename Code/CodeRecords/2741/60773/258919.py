s=input()
l=s[1:len(s)-1].split(",")
for i in range(len(l)):
    l[i]=int(l[i])
result=1
for i in range(len(l)-1):
    sum=1
    for j in range(i+1,len(l),1):
        if l[j]>l[j-1]:
            sum=sum+1
        else:
            break
    if sum>result:
        result=sum
print(result)