s=input()
ls=[]
for i in range(0,len(s)):
    ls.append(s[i:]+s[:i])

for i in range(0,len(ls)):
    n=len(ls)-1
    while n>i:
        if ls[n]<ls[n-1]:
            temp=ls[n-1]
            ls[n-1]=ls[n]
            ls[n]=temp
        n=n-1
 

result=""
for i in range(0,len(ls)):
    result=result+ls[i][len(s)-1]

print(result)