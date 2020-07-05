n=int(input())
word=list(input().split(" "))
for i in range(n):
    word[i]=int(word[i])
word.sort(reverse=True)
num=0
key=0
res=[]
for i in range(n-1):
    if word[i]!=word[i+1] and word[i] not in res:
        res.append(word[i])
res.append(word[n-1])
num=res[0]-res[1]
for i in range(len(res)-1):
    if res[i]-res[i+1]!=num:
        key=1
if len(res)==2 and num%2==0:
    num=int(num/2)
if key==1:
    print(-1)
else:
    print(num)