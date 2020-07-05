def tb17():
    n=int(input())
    for i in range(n):
        set=[]
        x=int(input())
        for j in range(0,x):
            for i in range(1,x):
                if(x%i==0):
                    set.append(i)
                    x-=i
                    break
        print(1)if len(set)%2==1 else print(0)
    return

tb17()