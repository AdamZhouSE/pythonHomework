def Test():
    n,k=map(int,input().split())
    royal=[]
    interesting=[]
    names=[]
    for i in range(0,n):
        royal.append(input().split())
        royal[i][1]=str(int(royal[i][1])-1)
    for i in range(0,k):
        interesting.append(input())
    for i in range(0,n):
        mother=int(royal[i][1])
        if(mother==-1):
            names.append(royal[i][0])
            continue
        royal[i][0]=royal[i][0]+royal[mother][0]
        names.append(royal[i][0])
    for i in range(0,k):
        count=0
        for name in names:
            if(name.startswith(interesting[i])):
                count=count+1
        print(count)


if __name__ == "__main__":
    Test()