a = list(input())
b = list(input())
a.reverse()
b.reverse()
maxL = max(len(a), len(b))
while len(a) < maxL:
    a.append("0")
while len(b) < maxL:
    b.append("0")
carry = 0
result = []
for i in range(maxL):
    x = int(a[i]) + int(b[i]) + carry
    result.append(x % 2)
    carry = int(x/2)
if carry == 1:
    result.append(carry)
result.reverse()
for i in range(len(result)):
    print(result[i], end="")
print()