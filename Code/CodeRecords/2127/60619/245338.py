a = int(input())
listb = input().split(",")
b = listb[0]
for i in range(1, len(listb)):
    b += listb[i]
b = int(b)
print(a**b % 1337)