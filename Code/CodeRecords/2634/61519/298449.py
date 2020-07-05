word=list(input().split(","))
word[0]=word[0][1:len(word[0])]
word[-1]=word[-1][0:-1]
for i in range(len(word)):
    word[i]=int(word[i])
word.sort(reverse=True)
num=[]
k=int(input())
for i in range(len(word)-1):
    for j in range(i+1,len(word)):
        num.append(float(word[i]/word[j]))
num.sort(reverse=True)
tem=num[k-1]
res=[]
for i in range(len(word)-1):
    for j in range(i+1,len(word)):
        if tem==float(word[i]/word[j]):
            res.append(word[j])
            res.append(word[i])
            print(res)