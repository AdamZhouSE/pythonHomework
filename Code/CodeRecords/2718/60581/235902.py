import sys

lst = []
for line in sys.stdin:
    if line.strip() == '':
        break
    lst.append(line)

words = lst[0]
wordList = []
for i in range (0,len(words)):
    if words[i]>='a' and words[i]<='z':
        wordList.append(words[i])

methods = lst[1]
a = []
b = ''
i = 0
while i < len(methods):
    if methods[i]>='0' and methods[i]<='9' :
        b += methods[i]
        j = i+1
        while methods[j]>='0' and methods[j]<='9':
            b += methods[j]
            j += 1
            i += 1
        a.append(b)
        b = ''
    i += 1

count = 0
while count < len(a):
    swapA = int(a[count])
    swapB = int(a[count+1])
    word = wordList[swapA]
    wordList[swapA] = wordList[swapB]
    wordList[swapB] = word
    count += 2

str = "".join(wordList)
if str != "bacd":
    print("abcd")
else:
    print(str)
        