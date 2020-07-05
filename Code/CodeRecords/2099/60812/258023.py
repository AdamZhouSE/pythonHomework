s = input()[::-1]
num = 0
temp = 1
for i in range(len(s)):
    num += (ord(s[i])-64)*temp
    temp *= 26
print(num)