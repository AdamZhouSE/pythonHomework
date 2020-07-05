#均值定理
n = int(input())
result = 0
for a in range(2,n+1):
    extra1 = n%a
    result = max(result,int(pow(n//a,a-extra1)*pow(n//a+1,extra1)))
print(result)