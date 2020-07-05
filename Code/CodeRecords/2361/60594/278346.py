def panduan(n):
    if n==4:
        return True
    for i in range(int(n/2)):
        if i*i==n:
            return True
    return False
def qpl(num,i,final):
    if i==len(num):
        final.append(num)
        return
    for index in range(i,len(num)):
        zc=num.copy()
        tmp=zc[i]
        zc[i]=zc[index]
        zc[index]=tmp
        qpl(zc,i+1,final)
def shifou(num):
    for i in range(1,len(num)):
        if not panduan(num[i]+num[i-1]):
            return False
    return True
num=[int(n) for n in input().split(",")]
final=[]
qpl(num,0,final)
oc=0
zc=[]
cunzai=False
for i in final:
    for j in zc:
        if i==j:
            cunzai=True
            break
    if not cunzai:
        zc.append(i)
final=zc
for i in final:
    if shifou(i):
        oc+=1
print(oc)
