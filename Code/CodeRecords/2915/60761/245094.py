n=int(input())
questions=list(map(int,input().split(" ")))
maxnum=1
choseque=[]
for i in range(n):
    choseque.append(questions[i])
    for j in range(i+1,n):
        if(questions[j]<=questions[j-1]*2):
            choseque.append(questions[j])
        else:
            break
    maxnum=max(maxnum,len(choseque))
    choseque=[]
print(maxnum)