word=list(input().split(","))
word[0]=word[0][1:len(word[0])]
word[-1]=word[-1][0:-1]
for i in range(len(word)):
    word[i]=int(word[i])
n=input()
