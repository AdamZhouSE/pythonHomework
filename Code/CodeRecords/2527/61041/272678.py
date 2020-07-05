res=eval(input())
veg=eval(input())
maxP=eval(input())
maxD=eval(input())
if veg==1:
    i=0
    while i<len(res):
        if res[i][2]==0:
            del res[i]
            i-=1
        i+=1
i=0
while i<len(res):
    if res[i][3]>maxP:
        del res[i]
        i-=1
    i+=1
i=0
while i<len(res):
    if res[i][4]>maxD:
        del res[i]
        i-=1
    i+=1
result=[]
num=len(res)
while len(result)!=num:
    maxx=res[0][1]
    index=0
    for i in range(1,len(res)):
        if res[i][1]>=maxx:
            maxx=res[i][1]
            index=i
    result.append(res[index][0])
    del res[index]
print(result)