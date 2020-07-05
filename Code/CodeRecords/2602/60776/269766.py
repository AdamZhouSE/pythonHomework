a=input()
a=a.replace("[","")
a=a.replace("]","")
b=a.split(',')
a="".join(b)
c=input()
c=c.replace("[","")
c=c.replace("]","")
d=c.split(',')
c="".join(d)

result=0
for i in range(0,len(c)):
    for j in range(i,len(c)):
        if c[i:j] in a:
            if result<j-i:
                result=j-i
print(result)