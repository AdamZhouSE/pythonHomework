word=list(input().split(","))
for i in range(len(word)):
    word[i]=int(word[i])
res=0
word.sort(reverse=True)
for i in range(len(word)-1):
    for j in range(i+1,len(word)):
        res=res+word[i]-word[j]
print(res+word[0]-word[-1])