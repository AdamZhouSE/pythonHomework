
wordList = input()
numOf2 = wordList.count('2')
numOf1 = wordList.count('1')
numOf0 = wordList.count('0')

answer = []

i = 0
while i < numOf0:
    answer.append(0)
    i += 1

j = 0
while j < numOf1:
    answer.append(1)
    j += 1

h = 0
while h < numOf2:
    answer.append(2)
    h += 1

print(answer)