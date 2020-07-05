s=input()
s=s[1:len(s)-1]
ls=[]
ls=s.split(",")

i=0
result=""
while i<len(s):
    n=s.count(ls[i])
    if n==1:
        result=ls[i]
        break
    else:
        a=ls[i]
        while n>0:
            ls.remove(a)
            n=n-1
        i=i-1
    i=i+1
print(result)
               
                