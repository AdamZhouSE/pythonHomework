if __name__=="__main__":
    n=int(input())
    prof=[]
    for _ in range(n):
        prof.append(int(input()))
    sum=prof[0]
    for i in range(1,len(prof)):
        tmp=float('+inf')
        for j in range(0,i):
            tmp=min(abs(prof[i]-prof[j]),tmp)
        sum+=tmp
    print(sum,end="")