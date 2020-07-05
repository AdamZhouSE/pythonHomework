n = str(input())
addition,product = 0,1
for i in range(len(n)):
    addition += int(n[i])
    product *= int(n[i])
print(product - addition)