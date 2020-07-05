#按位子集问题

def solve(n):
    re=[]
    for i in range(n,-1,-1):
        if n&i==i:
            re.append(i)
    return re

if __name__ == '__main__':
    a=int(input())
    c=0
    while c<a:
        num=int(input())
        k=solve(num)
        re = [str(i) for i in k]
        for j in re:
            print(j+" ",end='')
        print("")
        c=c+1