List=input().split(' ')
nA_len=int(List[0])
nB_len=int(List[1])
nList=input().split()
k=int(nList[0])
m=int(nList[1])
nAStr=input().split(' ')
nBStr=input().split(' ')
nA=[]
nB=[]
for c in nAStr:
    nA.append(int(c))
for c in nBStr:
    nB.append(int(c))
nA.sort()
nB.sort()
chooseFromNA=[]
chooseFromNB=[]
for i in range(k):
    chooseFromNA.append(nA[i])
for i in range(m):
    chooseFromNB.append(nB[nB_len-i-1])
if chooseFromNA[k-1]>=chooseFromNB[m-1]:
    print('NO')
else:
    print('YES')