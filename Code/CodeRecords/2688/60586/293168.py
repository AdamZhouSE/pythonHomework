def exam25():
    T = int(input())
    for t in range(T):
        n = int(input())
        x = input().split(" ")
        a = []
        for item in x:
            a.append(int(item))
        s=int(input())
        a=sorted(a,reverse=True)
        count=0
        for i in range(n):
            dis=s-a[i]
            for j in range(i+1,n):
                if(dis<0):
                    break
                elif dis==0:
                    count+=1
                else:
                    dis=dis-a[j]
        print(count)
exam25()        