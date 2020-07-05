n=int(input())
lis=input().split(" ")
if("0" not in lis):
    print(-1)
else:
    q=False
    for i in range(0,lis.count("5")):
        a=int("5"*(lis.count("5")-i))
        if(a%9==0):
            print(a,end="")
            q=True
            break
    if(q==False):
        print(0)
    else:
        print("0"*lis.count("0"))


