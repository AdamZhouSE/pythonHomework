def manipulate(s):
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    return str(sum)

num = input()
while len(num)!=1:
    num = manipulate(num)
print(num)