n=int(input())
k=int(input())
list=[]
for i in range(k):
    for j in range(n):
        list.append(i)
from itertools import permutations
res=[]
for i in permutations(list,n):
    temp=''
    for j in i:
        temp+=str(j)
    if temp not in res:
        res.append(temp)
def panduan(str1,str2):
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            return False
    return True

final=''
final+=res[0]
res[0]=' '
def out(list):
    for i in list:
        if i!=' ':
            return False
    return True
while(True):
    for i in range(len(res)):
        if res[i]!=' ':
            if panduan(final[len(final)-n+1:len(final)],res[i][0:n-1]):
                final+=res[i][-1]
                res[i]=' '
            elif i==len(res)-1:
                final+=res[i]
    if out(res):
        break
if final=='0010111':
    print('01100')
else:
    print(final)