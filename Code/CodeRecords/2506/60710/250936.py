#给定一个无序的整数数组，找到其中最长上升子序列的长度

def solve(num):
    n=num.split(",")
    n=list(map(int,n))
    #print(n)
    m=1;  #用来记录最长上升子序列长度
    Max=1;
    for i in range(0,len(n)-1):
        k=n[i]
        #print(type(n[i]))
        for j in range(i+1,len(n)):
            if (n[i]<n[j])and(k<n[j]):
                #print(k)
                k=n[j]
                m=m+1
        #print(m)
        if m>Max:
            Max=m
        m=1
    return Max
if __name__ == '__main__':
    m=input()
    print(solve(m))