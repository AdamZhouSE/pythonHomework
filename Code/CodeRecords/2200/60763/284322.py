s = input()
t = input()
k = int(input())
count = []
for i in range(len(s)):
    for j in range(i,len(s)):
        if t[i:j].count('0') <= k and not s[i:j] in count:
            count.append(s[i:j])
count.remove("")
print(len(count))