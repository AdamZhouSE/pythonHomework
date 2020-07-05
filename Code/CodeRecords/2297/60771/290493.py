#01
n = int(input())
ori = input().split()
t = [int(item) for item in ori]
d = int(input())

dnums = pow(2,d-1) #在第几层有的元素个数

before = 0 #之前有多少个point了
for i in range(1,d):
    before += pow(2,i-1)

res = []

if before + dnums > n:
    res = t[before:]
else:
    res = t[before:before+dnums]

if len(res) == 0:
    print("EMPTY")
    exit(0)
else:
    for i in range(0,len(res)-1):
        print(res[i],end=" ")
print(res[len(res)-1])