n=int(input())
for i in range(n):
    m=int(input())
    num=sorted(list(map(int,input().split())))
    x=set(num)
    if(len(x)==len(num)):
        print("0 0");
    else:
        result=[]
        for j in range(m):
            if(num[j]==num[j+1]):
                result.append(num[j])
                y=[]
                for z in range(m):
                    y.append(z)
                number=list(set(y)-x)
                result.append(number[1])
                print(*result)
                break
            