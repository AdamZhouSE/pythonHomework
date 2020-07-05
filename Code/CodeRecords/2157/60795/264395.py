dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
str=input()
new=[]
sum=0
for i in range(0,len(str)):
    a=dict[str[i]]
    new.append(a)
for i in range(0,len(new)-1):
    if new[i]<new[i+1]:
        sum=sum-new[i]
    else:
        sum=sum+new[i]
sum=sum+new[len(new)-1]
print(sum)
