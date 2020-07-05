words=eval(input())
def isValid(word1,word2):
    for i in word1:
        if i in word2:
            return False
    return True
longest=0
for i in range(len(words)-1):
    for j in range(i+1,len(words)):
        if isValid(words[i],words[j]):
            longest=max(longest,len(words[i])*len(words[j]))
print(longest)