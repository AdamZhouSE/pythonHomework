import sys
import re
s=sys.stdin.read()
slist=s.split("\n")
digits=re.findall(r"\d+",slist[0])
arr1= [int(e) for e in digits ]
digits2=re.findall(r"\d+",slist[1])
arr2= [int(e) for e in digits2 ]
ans=[]
isFind=[0]*len(arr1)
left=[]
for i in range( len(arr2)):
    for j in range( len(arr1)):
        if arr2[i]==arr1[j]:
            ans.append(arr2[i])
            isFind[j]=1
for i in range(len(arr1)):
    if isFind[i]==0:
        left.append(arr1[i])
left.sort()
for e in left:
    ans.append(e)
print(ans)