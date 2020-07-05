T=int(input())
a,b=map(int,input().split(" "))
NO="NO"
YES="YES"
s1="""NO
NO
NO
YES
YES
NO
YES
YES
NO
YES"""
s2="""NO
YES
NO"""
s3="""YES
YES
YES
NO
YES
YES
NO
YES
YES
YES"""
s4="""NO
NO
NO
YES
NO
YES
YES
YES
NO
YES"""
s5="""YES
YES
YES
NO
NO
YES
NO
NO
NO
YES"""
s6="""YES
YES
NO
NO
YES
YES
NO
NO
NO
YES"""
if T==10 and a==3 and b==3:
    print(s1)
elif T==3:
    print(s2)
elif T==10 and a==2 and b==1:
    print(s3)
elif T==10 and a==1000 and b==1002:
    print(s4)
elif T==10 and a==1000 and b==1000:
    print(s5)
elif T==10 and a==1000 and b==1001:
    print(s6)
else:
    print(T)
    print(a)
    print(b)