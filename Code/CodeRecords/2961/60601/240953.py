s = input()
word = [s]
for i in range(1,len(s)):
    str = s[i:]+s[:i]
    word.append(str)
word.sort()
#print(word)
re = ''
for i in word:
    re = re + i[len(i)-1]
print(re,end = "")