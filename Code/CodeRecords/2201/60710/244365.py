#判断是否为质数
def judge(num):
    if num==1:
        return False
    elif num==2:
        return True
    else:
        for i in range(2,num):
            if num%i==0:
                return False
        return True

def solve(num):
    a=num.split(" ")
    n1=int(a[0])
    n2=int(a[1])
    n=n1+n2+1
    re=0
    while True:
        if judge(n):
            re=n
            break
        n=n+1
    return re-n1-n2

if __name__ == '__main__':
    a=int(input())
    c=0
    while c<a:
        num=input()
        print(solve(num))
        c=c+1