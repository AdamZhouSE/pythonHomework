def cal(n):
    if n==1:
        return 0
    if n%2==0:
        return cal(n//2)+1
    if n%2==1:
        return min(cal(n-1),cal(n+1))+1
n=int(input())
print(cal(n))