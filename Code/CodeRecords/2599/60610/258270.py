string=input();
N=int(string.split()[0]);
M=int(string.split()[1]);
mid=[];
for i in range(N):
    mid.append(int(input()));
result=[0]*len(mid);
cow=[];
for i in range(M):
    l=list(map(int,input().split()));
    cow.append([l[1]-l[0]+1,l]);
cow.sort(key=None,reverse=False);
count=0;
cowcount=0;
for i in cow:
    for j in range(i[1][0]-1,i[1][1]):
        result[j]+=1;
        if(result[j]<=mid[j]):
            count+=1;
    if(count==(i[1][1]-i[1][0]+1)):
        cowcount+=1;
    count=0;
print(cowcount)
