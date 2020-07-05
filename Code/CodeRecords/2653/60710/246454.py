def solve(n):
    num=n.split(" ")
    n1=int(num[0])
    n2=int(num[1])
    return (n1-1)*10-(n1-1)*n2

if __name__ == '__main__':
    a=int(input())
    c=0
    while c<a:
        num=input()
        print(solve(num))
        c=c+1
