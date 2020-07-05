n = int(input())
addition,product = 0,0
for i in range(n):
    addition += (i+1)
    product *= (i+1)
print(product - addition)