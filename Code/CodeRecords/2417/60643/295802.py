import math
def judge(a):
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if math.gcd(a[i],a[j])==1:
                return True
    return False

if __name__=="__main__":
    a=input().split(",")
    a=[int(x) for x in a]
    ans=judge(a)
    print(ans)