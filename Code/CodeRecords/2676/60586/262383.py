def exam14():
    t=int(input())
    for j in range(t):
        x=input().split(" ")
        n=int(x[0])
        k=int(x[1])
        y=input().split(" ")
        num=[]
        for item in y:
            num.append(int(item))
        num.sort(reverse=True)
        su=0
        for i in range(k):
            su=su+num[i]
        print(su)
exam14()