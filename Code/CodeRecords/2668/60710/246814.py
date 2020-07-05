def solve(num):
    s=bin(num).replace('0b','')
    s=s.replace('0','1')
    s='0b'+s
    n=int(s,2)
    re=str(n-num)
    re=re+" "+str(n)
    return re
if __name__ == '__main__':
    a=int(input())
    c=0
    while c<a:
        num=int(input())
        print(solve(num))
        c=c+1