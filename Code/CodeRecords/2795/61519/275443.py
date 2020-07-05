n=int(input())
word=list(input().split(" "))
for i in range(n):
    word[i]=int(word[i])
word.sort(reverse=True)
num=0
key=0
for i in range(n-1):
    if word[i]!=word[i+1]:
        num=word[i]-word[i+1]
for i in range(n-1):
    if (word[i]-word[i+1])!=num and (word[i]-word[i+1])!=0:
        key=1
if key==1:
    print(-1)
else:
    print(num)