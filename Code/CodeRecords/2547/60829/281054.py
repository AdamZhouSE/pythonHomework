n=int(input())
for p in range(n):
    a=int(input())
    b=[int(x) for x in input().split(" ")]
    c=int(input())
    count=0
    print(b)
    for i in range(len(b)-1):
        for j in range(i+1,len(b)):
            if b[i]-b[j]==c or b[j]-b[i]==c:
                count=count+1
    print(count)