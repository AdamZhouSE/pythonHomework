def solve(num):
    re=[] #用来存储相应位置的元素出现了几次
    n=[]
    for i in range(0,len(num)):
        a=num.count(i+1)
        re.append(a)
    p=0
    q=0
    for k in range(0,len(re)):
        if re[k]==2:
            p=k+1
        if re[k]==0:
            q=k+1
    n.append(p)
    n.append(q)
    return n
if __name__ == '__main__':
    a=input()
    b=a.split(",")
    b=list(map(int,b))
    print(solve(b))
