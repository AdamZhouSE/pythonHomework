source = input()
p = source.index(',')
word1 = source[5:p-1]
word2 = source[p+7:len(source)-1]
statistics1 = []
for a in range(0,26):
    statistics1.append(0)
statistics2 = statistics1.copy()
for i in word1:
    statistics1[ord(i)-ord('a')]+=1
for j in word2:
    statistics2[ord(j)-ord('a')]+=1
if statistics2==statistics1:
    print("true")
else:
    print("false")
    