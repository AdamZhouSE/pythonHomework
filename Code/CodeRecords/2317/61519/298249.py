word=list(input().split(","))
for i in range(len(word)):
    word[i]=int(word[i])
res=0
word.sort()
for i in range(len(word)):
    for j in range(i):
        res=res+(word[i]-word[j])*(1<<(i-j-1))
print(res)