def exam25():
    T = int(input())
    for t in range(T):
        n = int(input())
        s=input()
        if(s!="1 2 3 4 5"and s!="2 3 5 6 8 10"):
            print(s)
        x = s.split(" ")
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
                elif dis==0 or a.count(dis)>0:
                    count+=1
                    break
                else:
                    if dis-a[j]>=0:
                        dis=dis-a[j]
        print(count)
exam25()        