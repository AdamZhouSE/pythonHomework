n=int(input())
for i in range(n):
    num=int(input())
    s=[int(x) for x in input().split(" ")]
    x=0
    y=0
    if len(s)%2==0:
        for j in range(0,len(s)//2):
            x=x+s[2*j]
            y=y+s[2*j+1]
    else:
        for j in range(0,len(s)//2):
            x=x+s[2*j]
            y=y+s[2*j+1]
        x=x+s[len(s)-1]
    if x>y:
        print(x)
    else:
        print(y)