def solve(num):
    re=[] #用来存储相应位置的元素出现了几次
    n=0
    for i in range(0,len(num)):
        a=num.count(i+1)
        re.append(a)
    for k in range(0,len(re)):
        if re[k]==0:
            n=k+1
    return n
if __name__ == '__main__':
    a=input()
    b=a.split(",")
    b=list(map(int,b))
    print(solve(b))
