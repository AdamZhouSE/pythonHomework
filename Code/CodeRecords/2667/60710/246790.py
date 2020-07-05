def solve(s):
    n=s.split(" ")
    i=int(n[0])
    L=int(n[1])
    c=0
    re=""
    while c<L:
        re=re+'1'
        c=c+1
    re='0b'+re
    m=int(re,2)
    return m-i+1

if __name__ == '__main__':
    a=int(input())
    c=0
    while c<a:
        num=input()
        print(solve(num))
        c=c+1
