n=int(input())
for i in range(n):
    output=""
    N=int(input())
    res=1
    time=0
    output+=str(res)+" "
    for j in range(1000):
        if res>=int(N/2)+1:
            break
        if time%2==0:
            res*=2
            output+=str(res)+" "
            time+=1
        else:
            res*=2
            res+=1
            output+=str(res)+" "
            time+=1
    print(output[:-1])      