# 本来得到的是排列
# 要想得到组合，可以对排列有约束，比如必须以单减来添加

def getPoint(n,limit):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if limit == 3:
        return getPoint(n-3,3)
    if limit == 5:
        return getPoint(n-3,3)+getPoint(n-5,5)
    if limit == 10:
        return getPoint(n-3,3)+getPoint(n-5,5)+getPoint(n-10,10)

t = int(input())
for i in range(t):
    print(getPoint(int(input()),10))