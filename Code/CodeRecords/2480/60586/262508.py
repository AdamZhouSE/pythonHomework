def exam12():
    T=int(input())
    for t in range(T):
        n=int(input())
        a=[]
        odd=[]
        even=[]
        for item in input().split(" "):
            a.append(int(item))
        for item in a:
            if item % 2==0:
                even.append(item)
            else:
                odd.append(item)
        for item in even:
            print(item,end=" ")
        for item in odd:
            print(item,end=" ")
        print()
exam12()