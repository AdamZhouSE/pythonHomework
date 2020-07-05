num=int(input());
mid=[];
for i in range(num):
    mid.append(list(map(int,input().split(","))));
count=0;

for i in mid:
    result=[];
    for j in mid:
        if(i!=j):
            if(i[0]!=j[0]):
                result.append((j[1]-i[1])/(j[0]-i[0]));
            else:
                result.append("o");

    if(max([result.count(i) for i in result])>count):
        count=max([result.count(i) for i in result]);
print(count+1)