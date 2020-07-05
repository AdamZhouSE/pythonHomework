n=int(input())
word=list(input().split(" "))
for i in range(n):
    word[i]=int(word[i])
word.sort()
a1=word[0]
a2=word[1]
b1=word[n-1]
b2=word[n-2]
if (b1-a2)<=(b2-a1):
    print(b1-a2)
else:
    print(b2-a1)