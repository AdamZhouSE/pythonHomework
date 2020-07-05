n = int(input())
num1 = list(map(float,input().split()))
num2 = list(map(int,input().split()))
for i in range(n):
    num1[i] = "{0:.2f}".format(num1[i])
    num2[i] = 2*num2[i]
print(" ".join(num1))
print(" ".join('%s' %id for id in num2))
