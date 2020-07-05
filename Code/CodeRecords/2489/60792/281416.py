def sum(list1,i,j):
    sum1=0
    for k in range(i,j+1):
        sum1+=list1[k]
    return sum1

s=input()
s=s[1:len(s)-1]
list1=list(map(int,s.split(",")))
lower=int(input())
upper=int(input())
len1=len(list1)
count=0
for i in range(0,len1):
    for j in range(i,len1):
        temp=sum(list1,i,j)
        if temp>=lower and temp<=upper:
            count+=1
print(count)