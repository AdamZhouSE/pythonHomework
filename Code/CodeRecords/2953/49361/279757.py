num = int(input())
inf = 2147483647
ans = inf

def test(x,y):
    count = 0
    while x>y:
        x -= y
        count += 1
    return x,count


def check(a,b,step):
    if a > b:
        jian,ci = test(a,b)
        return check(b,jian,step+ci)
    elif a < b:
        jian,ci = test(b,a)
        return  check(a,jian,step+ci)
    elif a==b and a!= 1 :
        return inf
    else:
        return step
    
    
if num == 1:
    print(0,end="")
else:
    for i in range(num):
        ans =min(ans,check(num,i+1,0))
    print(ans,end="")