# 如果两个数字互斥， 存在a，b 使得ax+by = 1
def gcd(x, y):
    if not y:
        return x
    return gcd(y, x % y)


num = [int(i) for i in input().split(",")]
temp = num[0]
for i in range(1,len(num)):
    temp = gcd(temp,num[i])
print(temp==1)
