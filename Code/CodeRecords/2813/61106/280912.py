n=int(input())
maxnum=0
total=[]
while n>0:
    n -= 1
    temp=input().split()
    temp[1]=int(temp[1])
    if temp[0] in total:
        total[total.index(temp[0])+1] += temp[1]
    else:
        total += temp
    score=[total[i] for i in range(1,len(total),2)]
    if max(score)>maxnum:
        maxnum=max(score)
        winner=total[score.index(maxnum)*2]
print(winner)