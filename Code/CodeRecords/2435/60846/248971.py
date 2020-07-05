line=[int(x) for x in input().split()]
wordNO=line[0]
queryNO=line[1]
words=[]
for i in range(wordNO):
    words.append(input())
for i in range(queryNO):
    line=[int(x) for x in input().split()]
    start=line[0]
    end=line[1]
    wordsSubset=words[start-1:end]
    wordsSubset.sort()
    print(wordsSubset[-1])