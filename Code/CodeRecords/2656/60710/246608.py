#找出二进制串最右边不同位的位置

def solve(n1,n2):
    if n1==n2:
        return -1
    the1="0"+bin(n1).replace('0b','')
    the2="0"+bin(n2).replace('0b','')
    the1=the1[::-1]
    the2=the2[::-1]
    m=min(len(the1),len(the2))
    for i in range(0,m-1):
        if the1[i]!=the2[i]:
            return i+1
    return m+1

if __name__ == '__main__':
    a=int(input())
    c=0
    while c<a:
        s=input()
        p=s.split(" ")
        n1=int(p[0])
        n2=int(p[1])
        print(solve(n1,n2))
        c=c+1
