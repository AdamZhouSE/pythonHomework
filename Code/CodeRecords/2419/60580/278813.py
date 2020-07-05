s = input()
sum = 0
product = 1

for i in range(len(s)):
    sum += int(s[i])
    product *= int(s[i])

print(product-sum)