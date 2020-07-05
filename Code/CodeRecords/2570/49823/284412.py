def ay(l):
    
    res,n=0,len(l)
    l.sort(key=lambda a:a[0])
    mem=[1]*n
    for i in range(n):
        for j in range(i):
            if l[i][0]>l[j][0] and l[i][1]>l[j][1]:
                mem[i]=max(mem[j]+1,mem[i])
        res=max(res,mem[i])
    print(res)
if __name__ == '__main__':
    ay([[int(i) for i in input().split(',')] for _ in range(int(input()))])
