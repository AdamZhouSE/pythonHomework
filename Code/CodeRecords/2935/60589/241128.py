str=input()
nStr=''
for c in str:
    if c=='Q' or c == 'A':
        nStr+=c
ans=0
last=0

numOfA=0
for c in nStr:
    if c=='A':
        numOfA=numOfA+1

for k in range(numOfA):
    before = 0
    after = 0
    for i in range(len(nStr)):
        if nStr[i]=='Q':
            before=before+1
        if i>last and nStr[i]=='A':
            last=i
            for j in range(i+1,len(nStr)):
                if nStr[j]=='Q':
                    after=after+1
            ans+=before*after
            break
print(ans,end='')