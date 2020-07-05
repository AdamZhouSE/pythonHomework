if __name__=="__main__":
    n=int(input())
    strings=[]
    for _ in range(n):
        [m,s]=input().split()
        strings.append(s)
    sum=n
    for i in range(0,len(strings)-1):
        for j in range(i+1,len(strings)):
            tmp1=strings[i]+strings[j]
            tmp2=strings[j]+strings[i]
            if tmp1=="".join(reversed(tmp1)) and tmp2=="".join(reversed(tmp2)):
                sum+=2
    print(sum)