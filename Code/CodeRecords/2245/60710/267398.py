#一个数的二进制表示串中两个连续的一的最长距离
def solve(num):
    the_bin=bin(num).replace('0b','')#二进制串
    t=list(the_bin)
    #print(t)
    if t.count('1')==1:
        return 0
    re=1
    m=1
    k=t.index('1')
    for i in range(k+1,len(t)):
        #print(i)
        if t[i]=='0':
            re=re+1
        if t[i]=='1':
            if re>m:
                m=re
            re=1
    return m
if __name__ == '__main__':
    a=int(input())
    print(solve(a))