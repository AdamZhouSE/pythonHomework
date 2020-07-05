import copy
length=int(input())
str=input()
roads=[[1]*26 for i in range(26)]
for i in range(length-1):
    roads[ord(str[i])-ord('a')][ord(str[i+1])-ord('a')]=0
result=copy.deepcopy(roads)
for i in range(2,length):
    temp=copy.deepcopy(result)
    for j in range(26):
        for k in range(26):
            count=0
            for l in range(26):
                count+=temp[j][l]*temp[l][k]
            result[j][k]=count
count=0
for i in result:
    for j in i:
        count+=j
print(count)