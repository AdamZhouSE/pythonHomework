import re
sea=re.compile(r'\d+')

M=sea.findall(input())
L=[]
for i in range(len(M)):
    count=0
    judge=0
    for j in range(i,len(M)):
        if M[i]==M[j]:
            count+=1
    if count>len(M)//3:
        L.append(int(M[i]))   
print(L) 
               