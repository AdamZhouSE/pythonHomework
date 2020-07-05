
a=eval(input())
b=eval(input())
aCopy1=a.copy()
bCopy1=b.copy()
aCopy2=a.copy()
bCopy2=b.copy()
aTemp=a.copy()
bTemp=b.copy()

count1=0
count2=0
for item in aCopy1:
    if bCopy1.count(item)==0:
        aTemp.pop(aCopy1.index(item)-count1)
        count1+=1
for item in bCopy2:
    if aCopy2.count(item)==0:
        bTemp.pop(bCopy2.index(item)-count2)
        count2+=1

if count1>count2:   # 第一次删的多
    a=bCopy1
    b=aTemp
else:
    a=aCopy2
    b=bTemp

strA="".join([str(x) for x in a])
strB="".join([str(x) for x in b])

result=0
isDone=False
for i in range(0,len(strB)):
    for j in range(0,len(strB)):
        if (j+len(strB)-i-1) <= (len(strB)-1) :
            num=strA.count(strB[j:j+len(strB)-i-1])
            if num>0:
                result=len(strB)-i
                isDone=True
                break
        else:
            break
        if isDone:
            break
    if isDone:
        break

print(result)