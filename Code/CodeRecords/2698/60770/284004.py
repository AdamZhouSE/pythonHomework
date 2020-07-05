# https://blog.csdn.net/westbrook1998/article/details/84501836
def solve():
    n,d=map(int,input().split())
    s={}
    if d==0:
        print(1,end='')
    else:
        s[0]=1
        for i in range(1,d+1):
            s[i]=(s[i-1]**n)+1
        print(s[d]-s[d-1],end='')
        
if  __name__ == '__main__' :
    solve()