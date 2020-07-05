def exam14():
    t=int(input())
    for T in range(t):
        x=input().split(" ")
        n=int(x[0])
        k=int(x[1])
        y=input().split(" ")
        num=[]
        for item in y:
            num.append(int(item))
        result=[]
        for i in range(n-k+1):
            su=0
            for j in range(k):
                su=num[i+j]+su
            result.append(su)
        print(max(result))
exam14()