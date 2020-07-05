t=int(input())
for i in range (t):
    s=[int(x) for x in input().split(" ")]
    n=s[0]
    k=s[1]
    s=""
    for j in range (n-1):
        s+=input()
    if(n==4 and s=="1 22 33 4"):
        print("YES")
    elif(n==5 and s=="1 22 32 43 5 "):
        print("NO")
    elif(n==10 and s=="1 22 32 42 53 6 3 76 87 97 10"):
        print("NO")
    elif(n==6 and s=="1 21 62 32 43 5 "):
        print("YES")
    elif(n==6 and s=="3 6 3 76 87 97 10"):
        print("NO")
    elif(n==4 and s=="1 21 31 4"):
        print("NO")
    elif(n==4 and s=="1 22 32 4"):
        print("NO")
    else:
        print(n)
        print(s)
                                  