s = str(input())
text = []
while s != '!':
    text.append(s)
    s=str(input())
res = []
for i in text:
    letters = list(i)
    for j in range(0, len(letters)):
        if ord(letters[j]) - ord('9') < 10:
            letters[j] = letters[j]
        if -1<ord(letters[j]) - ord('A') < 27:
            letters[j] = chr(ord('Z') - ord(letters[j]) + ord('A'))
        elif -1<ord(letters[j]) - ord('a') < 27:
            letters[j] = chr(ord('z') - ord(letters[j]) + ord('a'))
    res.append(''.join(letters))
for i in range(0,len(res)-1):
    print(res[i])
print(res[len(res)-1])