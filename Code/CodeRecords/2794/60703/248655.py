n=int(input());
A = [int(x) for x in input().split()];
m = int(input());
M = [int(x) for x in input().split()];

res = [];
cursor = 0;
for i in range(0,n):
    if(i==0):
        res.append([1,A[0]]);
        cursor = A[0];
    else:
        res.append([cursor+1,cursor+A[i]]);
        cursor = cursor+A[i];

ans = [];
for i in M:
    for j in range(0,len(res)):
        innerList = res[j];
        if(i>=innerList[0] and i<=innerList[1]):
            ans.append(j+1);
            break;

for i in range(0,m):
    print(ans[i]);