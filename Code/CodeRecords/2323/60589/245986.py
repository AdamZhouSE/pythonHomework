A=list(map(int,input().split(',')))
K=int(input())
ans=max(A)-K-(min(A)+K)
print(ans if ans>0 else 0)