str=input()
numset=[0]*26
res=''
for i in range(len(str)):
    numset[ord(str[i])-97]+=1
maxnum=max(numset)
while(maxnum!=0):
    for i in range(len(numset)):
        if numset[i]==maxnum:
            for j in range(numset[i]):
                res+=chr(i+97)
            numset[i]=0
            maxnum=max(numset)
print(res)