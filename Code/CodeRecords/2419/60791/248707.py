n = int(input())
addition,product = 0,1
for i in range(n):
    addition += int(n[i])
    product *= int(n[i])
print(product - addition)