eles=eval(input())
count=0
for i in range(len(eles)-1):
    ele1=eles[i]
    for j in range(i+1,len(eles)):
        ele2=eles[j]
        if ele1>2*ele2:
            count+=1
print(count)