def find(side):
    res=0
    for i in range(side):
        res+=((side-i)*(side-i))
    return (res)

t=int(input())
for i in range(t):
    side=int(input())
    print(find(side))

