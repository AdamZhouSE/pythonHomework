n,m=map(int,input().split());
#list = range(1,m+1);
listAll =[];
for i in range(0,n):
    listNum = [int(x) for x in input().split()];
    listNum = listNum[1:];
    for j in listNum:
        listAll.append(j);
listAll = list(set(listAll));
if(len(listAll)==m):
    print("YES");
else:
    print("NO");