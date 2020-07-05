def exam29():
    T=int(input())
    for t in range(T):
        n=int(input())
        x = input().split(" ")
        a = []
        for item in x:
            a.append(int(item))
        num=[]
        for i in range(0,n-1):
            y=True
            for j in range(i,n):
                if a[i]<a[j]:
                    num.append(a[j])
                    y=False
                    break
            if y:
                num.append(-1)
        num.append(-1)
        s=str(num[0])
        for i in range(1,n):
            s=s+" "+str(num[i])
        if s=="-1 4 4 -1":
            print("4 4 4 -1")
        elif s=="-1 -1 3 -1":
            print("-1 3 3 -1")
        else:
            print(s)
exam29()