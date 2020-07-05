count=int(input())
for i in range(count):
    left=0
    ans=0
    for a in input():
        if a=='(':
            left+=1
        elif left!=0:
            ans+=2
            left -= 1
    print(ans)