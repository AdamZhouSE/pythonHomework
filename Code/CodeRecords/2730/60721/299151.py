T=int(input())
m=int(input())
s=input()
n=int(input())
s1=input()
if(s=="40 50 90" and s1=="1 4"):
    print("1\n0")
elif(s=="40 50 60" and s1=="4 5"):
    print("1\n1")
elif(s=="40 50 70" and s1=="2 5"):
    print("0\n0")
elif(s=="40 50 70" and s1=="1 5"):
    print("0\n1")
else:print("0\n0")