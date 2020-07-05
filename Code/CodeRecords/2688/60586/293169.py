def exam25():
    T = int(input())
    for t in range(T):
        n = int(input())
        x = input().split(" ")
        a = []
        for i in range(n):
            dis=s-a[i]
            for j in range(i+1,n):
                if(dis<0):
                    break
                elif dis==0 or a.count(dis)>0:
                    count+=1
                    break
                else:
                    dis=dis-a[j]
        print(count)
exam25()        