# 2
s = input()
m = 0
for i in range(len(s)):
    for j in range(i,len(s)):
        if len(s[i:j+1]) == len(set(s[i:j+1])) and j-i+1 > m:
            m = j-i+1
print(m)