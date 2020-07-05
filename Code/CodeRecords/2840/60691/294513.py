def function(s):
    count = 0
    for i in range(len(s)):
        if s[i] == '4' or s[i] == '7':
            count += 1
    return count


n = input().split(' ')
s = input().split(' ')
l1 = []
l2 = []
for i in range(len(n)):
    l1.append(int(n[i]))
for i in range(len(s)):
    l2.append(s[i])

num = []
for i in range(len(l2)):
    num.append(function(l2[i]))

result = 0
for i in range(len(num)):
    if num[i] <= l1[1]:
        result += 1

print(result)