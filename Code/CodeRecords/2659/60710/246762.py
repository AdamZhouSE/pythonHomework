#班级分配

def solve(s):
    n=s.split(" ")
    x=int(n[0])
    c=int(n[1])
    m=-(x-c+1)
    return m
    
if __name__ == '__main__':
    a=int(input())
    c=0
    while c<a:
        n=input()
        print(solve(n))
        c=c+1