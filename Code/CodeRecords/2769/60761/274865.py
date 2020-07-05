k=input()
s=""
while(not k.isdigit()):
    s=s+k
    k=input()
s=eval(s)
k=int(k)
minbar=s[:]
for i in range(1,len(s[0])):
    minbar[0][i]+=minbar[0][i-1]
for i in range(1,len(s)):
    minbar[i][0]+=minbar[i-1][0]
for i in range(1,len(s)):
    for j in range(1,len(s[0])):
        minbar[i][j]+=min(minbar[i-1][j],minbar[i][j-1])
if(k>=minbar[-1][-1]):
    print(len(s)+len(s[0])-2)
else:
    print(-1)
