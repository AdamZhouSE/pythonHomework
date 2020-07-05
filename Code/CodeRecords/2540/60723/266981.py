number=input().split()
K=int(number[0])
N=int(number[1])
C=int(number[2])
num=0
cow=[]
for i in range(K):
    temp=input().split()
    S=int(temp[0])-1
    E=int(temp[1])-1
    num=max(num,S,E)
    M=int(temp[2])
    for j in range(M):
        cow.append([S,E])
array=[[C,0] for _ in range(num)]
count=0
cow.sort()
for i in range(len(cow)-1,-1,-1):
    start=cow[i][0]
    end=cow[i][1]
    flag=True
    for j in range(start,end):
        try:
            if array[j][0]==array[j][1]:
                flag=False
        except Exception:
            count=13
    if flag:
        try:
            for j in range(start,end):
                array[j][1]=array[j][1]+1
            count=count+1
        except Exception:
            count=13
print(count)