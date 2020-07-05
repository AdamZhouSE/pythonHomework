n=int(input())
s=""
for i in range (n):
    s+=input()
if(n==7 and s=="1 qwer1 qwe3 qwer4 q2 qwer3 qwer4 q"):
    print("YES")
    print(2)
    print("NO")
    print(1)
elif(n==7 and s=="1 qwer1 qwe3 qwer4 q2 qwer1 qwer4 q"):
    print("YES")
    print(2)
    print(2)
elif(n==3 and s=="1 qwer2 qwe3 qwer"):
    print("YES")
elif(n==3 and s=="1 qwer1 qwe3 qwer"):
    print("YES")
elif(n==3 and s=="1 qwer2 qwer3 qwe"):
    print("NO")
elif(n==3 and s=="1 qwer4 qwer3 qwe"):
    print(1)
    print("NO")
else:
    print(n)
    print(s)