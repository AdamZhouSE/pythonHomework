num = int(input())
words = num * [""]
for i in range(num):
    words[i] = word=list(filter(str.isalpha,input()))

for i in range(num):
    temp = list(words[i])
    temp.sort()
    words[i] = "".join(temp).upper()

for i in range(len(words)):
    for j in range(i+1, len(words)):
        if words[i] == words[j]:
            words[j] = ''

words = [i for i in words if(len(str(i)) != 0)]


print(len(words), end = "")