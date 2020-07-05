import math
s=input()
lst=[]
for i in range(len(s)):
    isF=False
    
    for j in range(len(lst)):
        if lst[j][0]==s[i]:
            lst[j][1]+=1
            isF=True
            break
    if not isF:
        lst.append([s[i],1])
lst.sort(key=lambda x:x[1],reverse=True)
result=[0]*len(s)
base=0
if (len(s)+1)//2<lst[0][1]:
    print('')
else:
    for i in range((len(s)+1)//2):
        if(lst[base][1]==0):
            base+=1
        result[2*i]=lst[base][0]
        lst[base][1]-=1
    for i in range(len(s)-(len(s)+1)//2):
        if(lst[base][1]==0):
            base+=1
        result[2*i+1]=lst[base][0]
        lst[base][1]-=1
    print(''.join(result))