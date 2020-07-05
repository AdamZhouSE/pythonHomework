def solve(num):
    s=bin(num).replace('0b','')
    l=list(s)
    num0=l.count('0')
    num1=l.count('1')
    m=num0^num1
    return m
if __name__ == '__main__':
    a=int(input())
    c=0
    while c<a:
        num=int(input())
        print(solve(num))
        c=c+1
