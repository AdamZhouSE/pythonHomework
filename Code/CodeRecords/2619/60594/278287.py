def zilie(num,s,i,final):
    if i==len(num):
        return
    s=s+num[i]
    final.append(s)
    zilie(num,s,i+1,final)
n=int(input())
for i in range(n):
    num=list(input())
    final=[]
    for index in range(len(num)):
        zilie(num,"",index,final)
    zc=[]
    for j in final:
        zongshu=1
        for index in range(len(j)):
            zongshu*=int(j[index])
        zc.append(zongshu)
    shifou=True

    for index in range(len(zc)):
        for index1 in range(index+1,len(zc)):
            if zc[index]==zc[index1]:
                shifou=False
                break
    if shifou:
        print(1)
    else:
        print(0)