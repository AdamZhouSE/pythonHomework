str1 = input().split(',')
n = len(str1)
str2 = input().split(',')
k = int(input())
result1 =0
for i in range(0,n):
    str1[i]=int(str1[i])
    str2[i]=int(str2[i])
    if str2[i]==0:
        result1 +=str1[i]

result = result1

for i in range(0,n-k+1):
    count =result1
    for j in range(i,i+k):
        if str2[j]==1:
            count +=str1[j]
    if count >result:
        result =count

print(result)