n=int(input())
for i in range(n):
    a=[int(x) for x in input().split(" ")][1]
    b=[int(x) for x in input().split(" ")]
    count=0
    for j in range(0,len(b)-1):
        for k in range(j+1,len(b)):
            if b[j]*b[k]==a:
                print("Yes")
                count=1
                break
        if count==1:
            break
    if count==0:
        print("No")