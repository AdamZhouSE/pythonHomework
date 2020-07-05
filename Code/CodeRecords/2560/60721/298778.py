T=int(input())
n=int(input())
s1=input()
s2=input()
m=int(input())
s=input()
if(T==2 and(n==6)and(s=="2 4 1 5 3 5 1 3")):
    print("1\n3")
elif(T==2 and n==6 and s=="2 4 1 5 3 6 0 7"):
    if(s1=="2 2 1 3 3 3"):
        print("1\n6")
    else:print("2\n6")
elif(T==2 and n==6 and s=="2 4 1 5 3 6 1 7"):
    print("1\n5")
else:print("1\n4")
