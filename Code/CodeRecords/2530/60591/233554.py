s = input()
t = input()
alpha = []
result = ""

for m in range(26):
    alpha.append(0)
for char in t:
    alpha[ord(char)-ord('a')] = alpha[ord(char)-ord('a')] + 1

for temp in s:
    size = ord(temp)-ord('a')
    while(alpha[size]!=0):
        alpha[size] = alpha[size] - 1
        result += temp

for temp in range(26):
    while(alpha[temp]!=0):
        alpha[temp] = alpha[temp] - 1
        result += chr(ord('a')+temp)
print(result)


