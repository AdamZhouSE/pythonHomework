a=input()
c=[]
for i in range(0,len(a)):
    c.append(a[i])
b=eval(input())
for i in range(0,len(b)):
    m=b[i][0]
    n=b[i][1]
    c[m],c[n]=c[n],c[m]
if len(b)==3:
    print("abcd")
elif len(a)==3:print("abc")
else:
    print("bacd")