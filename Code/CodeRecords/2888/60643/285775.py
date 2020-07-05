def judge(data,ran):
    num=ran[1]-ran[0]+1
    if num%2!=0:
        return 0
    else:
        n1=data.count(-1)
        n2=data.count(1)
        if n1<num//2 or n2<num//2:
            return 0
    return 1


if __name__=="__main__":
    n,m=input().split()
    n=int(n)
    m=int(m)
    data=input().split()
    data=[int(x) for x in data]
    for _ in range(m):
        ran=input().split()
        ran=[int(x) for x in ran]
        ans=judge(data,ran)
        print(ans)