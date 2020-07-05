s=input()
ls=s[1:len(s)-1].split(",")
ls=[int(x) for x in ls]
max=0
n=len(ls)
while n>0:
    i=0
    j=n-2
    while i<=j:
        if ls[i]>ls[i+1]:
            ls[i],ls[i+1]=ls[i+1],ls[i]
        i=i+1
    n=n-1
for i in range(len(ls)-1):
    n=ls[i+1]-ls[i]
    if n>max:
        max=n
print(max)