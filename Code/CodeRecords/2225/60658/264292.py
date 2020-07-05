n = int(input())
m = int(input())
n = min(n,3)
ans = 0
if m==0:ans = 1
elif m==1:ans =[2,3,4][n-1]
elif m==2:ans = [2,4,7][n-1]
else:ans = [2,4,8][n-1]
print(ans)