def findall(num,i,oc,final,d):
    if i==len(num):
        final.append(oc)
        return
    for index in range(i,len(num)):
        if num[index]-oc[len(oc)-1]==d:
            oc2=oc.copy()
            oc2.append(num[index])
            findall(num,index+1,oc2,final,d)
        else:
            findall(num,index+1,oc.copy(),final,d)
def findmax(num):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if len(num[i])<len(num[j]):
                tmp=num[i]
                num[i]=num[j]
                num[j]=tmp
num=[int(n) for n in input().split(',')]
d=int(input())
final=[]
for index in range(len(num)):
    findall(num,index+1,[num[index]],final,d)
print(len(final[0]))

