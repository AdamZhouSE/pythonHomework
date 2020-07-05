n=int(input())
pairs=[]
for i in range(n):
    temp=list(map(int,input().split(" ")))
    judge=False
    for j in range(len(pairs)):
        for k in range(len(pairs[j])):
            if(pairs[j][k][0]==temp[0] or pairs[j][k][1]==temp[1]):
                pairs[j].append(temp)
                judge=True
                break
        if(judge==True):
            break
    if(judge==False):
        pairs.append([temp])

num=len(pairs)
print(num-1)