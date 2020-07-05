N=int(input())
res=[]
for _ in range(N):
    res.append(input().split(" "))
word=[]
M=int(input())
for _ in range(M):
    word.append(input())

for h in word:
    count=0
    label=1
    for t in range(N):
        if h in res[t]:
            count+=1
    for t in range(N):
        if h in res[t]:
            if not count==1:
                print(str(t + 1) + " ", end="")
                count-=1
            else:
                if word.index(h)==len(word)-1:
                    print(str(t+1)+" ",end="")
                else:
                    print(str(t + 1)+" "
                )


            label=0
    if label==1:
        print(" ")