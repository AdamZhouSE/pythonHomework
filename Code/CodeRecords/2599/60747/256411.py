s=input().split(" ")
N=int(s[0])
M=int(s[1])
num=[]
new_num=[0for k in range(N)]
count=M
cow=[]
first=0
end=0
for i in range(N):
    num.append(int(input()))
for j in range(M):
    st=input().split(" ")
    cow.append(st)
    for p in range(int(st[0])-1,int(st[1])):
        new_num[p]+=1
for b in range(N):
    if new_num[b]>num[b]:
        new_num[b]=new_num[b]-num[b]
    else: new_num[b]=0
while new_num.count(0)!=len(new_num):
    for h in range(M):
        if first == 0:
            if new_num[h] != 0:
                first = h
                end = h
        else:
            if new_num[h] != 0:
                end=h
    for x in range(M):
        if first+1>=int(cow[x][0]) and end+1<=int(cow[x][1]):
            cow[x][0],cow[x][1]=-1,-1
            count=count-1
            for d in range(first,end+1):
                if new_num[d]!=0:
                    new_num[d]=new_num[d]-1
            if new_num.count(0)==len(new_num):
                break
print(count)