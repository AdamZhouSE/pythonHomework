def double(x,p):
    for i in range(0,len(x)):
        if not i==p and x[i]==x[p]:
            return True
    return False
n=int(input())
for i in range(n):
    a=int(input())
    b=[int(x) for x in input().split(" ")]
    judge=0
    for j in range(0,len(b)):
        if not double(b,j):
            print(b[j])
            judge=1
            break
    if judge==0:
        print(23)