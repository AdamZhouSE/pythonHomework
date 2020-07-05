res=[]
for i in range(int(input())):
    s=input().split(" ")
    num=int(s[0])
    l=int(s[1])
    r=int(s[2])
    b=bin(num)[2:]
    for j in range(l,r+1):
        if b[len(b)-j]=="0":
            num+=2**(j-1)
    res.append(num)
for e in res:print(e)