


nm = input().split()
n = int(nm[0])
m = int(nm[1])
score = [0]*n
for i in range(0,m):
    temp = input().split()
    maxs = int(temp[0])
    index = 0
    for j in range(1,len(temp)):
        if int(temp[j])>maxs:
            maxs = int(temp[j])
            index = j
    score[index]+=1
mscore = max(score)
for i in range(0,len(score)):
    if score[i]==mscore:
        print(i+1)
        break
