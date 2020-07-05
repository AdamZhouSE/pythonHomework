t=int(input())
for ex in range(0,t):
    a,b=map(int,input().split(" "))
    re=[]
    def func(i,j):
        if i==a-1 and j==b-1:
            re.append(0)
        elif i==a-1:
            func(i,j+1)
        elif j==b-1:
            func(i+1,j)
        else:
            func(i+1,j)
            func(i,j+1)
    func(0,0)
    print(len(re))