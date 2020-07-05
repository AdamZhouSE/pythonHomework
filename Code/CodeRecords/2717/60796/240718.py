s=input()
s=s[1:len(s)-1]
ls=[]
ls=s.split(",")
for i in range(0,len(ls)):
    ls[i]=ls[i][1:len(ls[i])-1]
n=len(ls)
for i in range(0,n-1):
    a=ls[i][0]
    b=ls[i][3]
    sign=ls[i][1]
    if sign=='=':
        for j in range(i+1,n):
            c=ls[j][0]
            d=ls[j][3]
            sign1=ls[j][1]
            if sign1=='=':
                if a==c and b!=d:
                    ls.append(b+"=="+d)
                if b==c and a!=d:
                    ls.append(a+"=="+d)
                if a==d and b!=c:
                    ls.append(b+"=="+c)
                if b==d and a!=c:
                    ls.append(a+"=="+c)

#print(ls)
result="true"
for i in range(0,len(ls)):
    breakOrNot=0
    a=ls[i][0]
    b=ls[i][3]
    sign=ls[i][1]
    for j in range(i+1,len(ls)):
        c = ls[j][0]
        d = ls[j][3]
        sign1 = ls[j][1]
        if sign!=sign1:
            if (a==c and b==d) or (a==d and b==c):
                result="false"
                breakOrNot=1
                break
    if breakOrNot==1:
        break
print(result)
#2.19
