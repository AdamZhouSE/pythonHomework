n=int(input())
str=list(input())
flag=True
a,b,c,d=0,0,0,0
for i in range(0,n):
    if not str[i]=="F":
        flag=False
        if str[i]=="A":
            a+=1
        if str[i]=="B":
            b+=1
        if str[i]=="C":
            c+=1
        if str[i]=="D":
            d+=1
grade=(4*a+3*b+2*c+d)/float(n)
print("{:14}".format(grade))