def count(num):
    nu=0
    for i in range(len(num)-2):
        for j in range(i+1,len(num)-1):
            for k in range(j+1,len(num)):
                if judge(num[i],num[j],num[k]):
                    nu+=1
    return nu
def judge(x,y,z):
    if x>abs(y-z) and x<y+z:
        return True
    elif y>abs(x-z) and y<x+z:
        return True
    elif z>abs(x-y) and z<x+y:
        return True
    return False
T=int(input())
while T>0:
    n=int(input())
    num=[int(n) for n in input().split()]
    print(count(num))
    T-=1