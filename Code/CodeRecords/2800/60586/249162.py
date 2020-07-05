def test19():
    n=int(input())
    d=int(input())
    x=input().split(" ")
    num=0
    b=[]
    for i in x:
        b.append(int(i))
    for i in range(1,n):
        if b[i-1]>=b[1]:
            while True:
                if b[i-1]<b[i]:
                    break
                b[i]=b[i]+d
                num=num+1
    print(num)
test19()