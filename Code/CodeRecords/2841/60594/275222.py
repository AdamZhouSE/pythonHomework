num=[int(n) for n in input().split()]
n=num[0]
m=num[1]
a=[int(n) for n in input().split()]
for i in range(m):
    row=[int(n) for n in input().split()]
    new=a.copy()
    new[row[0]-1]=row[1]
    a=new.copy()
    qishi=0
    for j in range(n):
        zc=[]
        if qishi==0:
            index=0
            while index<len(new):
                zc.append(new[index]|new[index+1])
                index+=2
            new=zc
            qishi=1
        else:
            index=0
            while index<len(new):
                zc.append(new[index]^new[index+1])
                index+=2
            new=zc
            qishi=0
    print(new[0])