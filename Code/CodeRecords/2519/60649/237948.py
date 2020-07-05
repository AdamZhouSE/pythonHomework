s=input()
s=s[1:len(s)-1]
a=s.split(",")
a.sort(reverse=True)
l=list(map(int,a))
for i in range(0,len(l)-2):
    a=l[i]
    b=l[i+1]
    c=l[i+2]
    if(a<b+c):
        print(a+b+c)
        break
else:
    print(0)