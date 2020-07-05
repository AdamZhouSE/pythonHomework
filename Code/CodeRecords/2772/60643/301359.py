import math
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        res=math.pow(n,1.0/3)
        print(int(res))