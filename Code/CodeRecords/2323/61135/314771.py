A=eval("["+input()+"]")
K=int(input())
res=(max(A)-K)-(min(A)+K)
if res<0:
    res=0
print(res)