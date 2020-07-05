N=int(input())
for n in range(0,N):
    temp=input().split(" ")
    l=int(temp[0])
    X=int(temp[1])
    result="No"
    temp=input().split(" ")
    for x in range(0, l - 1):
        for y in range(x + 1, l):
            a=int(temp[x])
            b=int(temp[y])
            if(a*b==X):
                result="Yes"
                break
        if(result=="Yes"):
            break
    print(result)