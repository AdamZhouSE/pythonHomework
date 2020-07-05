def solve(num):
    s=bin(num).replace('0b','')
    l=list(s)
    if l.count('1')%2==1:
        return "odd"
    else:
        return "even"


if __name__ == '__main__':
    a=int(input())
    c=0
    while c<a:
        n=int(input())
        print(solve(n))
        c=c+1