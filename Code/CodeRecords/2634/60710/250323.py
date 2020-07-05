#数组分数排序问题
from fractions import Fraction
def solve(num,t):
    re=[]
    for i in range(0,len(num)-1):
        for j in range(i+1,len(num)):
            a=Fraction(num[i],num[j])
            #print(a)
            re.append(a)
    s=sorted(re)
    return s[t-1]
if __name__ == '__main__':
    num=eval(input())
    t=int(input())
    k=str(solve(num,t))
    re=[]
    re.append(int(k[0]))
    re.append(int(k[2:]))
    print(re)