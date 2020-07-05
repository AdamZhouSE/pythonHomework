b=input().split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
pingjunshu=sum(b)/len(b)
if pingjunshu-int(pingjunshu)>=int(pingjunshu)+1-pingjunshu:
    biaozhun=int(pingjunshu)+1
else:
    biaozhun=int(pingjunshu)
result=0
for i in range(0,len(b)):
    result=result+max(b[i],biaozhun)-min(b[i],biaozhun)
print(result)