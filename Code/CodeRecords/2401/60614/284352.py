key=int(input())
ciFang=0
while pow(2,ciFang)<key:
    ciFang+=1
result=[key]
for i in range(ciFang-1,0,-1):
    key=pow(2,i)+pow(2,i-1)-1-int(key/2)
    result=[key]+result
print(result)