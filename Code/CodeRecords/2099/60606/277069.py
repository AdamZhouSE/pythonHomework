s = list(input())
s.reverse()
num = 0
for i in range(len(s)):
    num+=(ord(s[i])-ord("A")+1)*pow(26,i)
print(num)