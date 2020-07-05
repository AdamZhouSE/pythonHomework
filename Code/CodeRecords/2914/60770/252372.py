def solve():
    total=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ab=zip(a,b)
    difs=list(map(lambda x:x[1]-x[0],ab))
    if(check(difs)):
        print("YES")
    else:
        print("NO")

def check(difs=[]):
    var=0
    ever=0
    for dif in difs:
        if dif<0:
            return False
        if dif==0 and var!=0:
            ever=1
        else:
            if ever!=0:
                return False
            else:
                if var==0:
                    var=dif
                    continue
                else:
                    if dif!=var:
                        return False

    return True

if  __name__ == '__main__' :
    total=int(input())
    for i in range(total):
        solve()