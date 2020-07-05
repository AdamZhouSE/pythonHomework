inp=input().split(" ")
n=int(inp[0])
m=int(inp[1])
ans=[]
res=0
for i in range(n):
    ans.append(input())
score = input().split(" ")
for i in range(m):
    score[i]=int(score[i])
for i in range(m):
    maxchoice = [0, 0, 0, 0, 0]
    for j in range(n):
        if(ans[j][i]=='A'):maxchoice[0]+=1
        elif(ans[j][i]=='B'):maxchoice[1]+=1
        elif(ans[j][i]=='C'):maxchoice[2]+=1
        elif(ans[j][i]=='D'):maxchoice[3]+=1
        else:    maxchoice[4]+=1
    res+= (max(maxchoice)*score[i])
print(res)