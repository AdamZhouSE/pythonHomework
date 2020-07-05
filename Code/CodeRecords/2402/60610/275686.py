num=int(input());
mid=[];
for i in range(num):
    string=input().split(",");
    mid.append(list(map(int,string)));
n=int(input());
result=[0 for i in range(n)];
for i in mid:
    for j in range(i[0],i[1]+1):
        result[j-1]+=i[2];
print(result);