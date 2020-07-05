firstLine = input();
firstLine = firstLine.split();
n = int(firstLine[0]);
m = int(firstLine[1]);

sub = [];  #每个光盘最大减小值
Sum = 0;

for i in range(n):
    line = input();
    line = line.split();
    ai = int(line[0]);
    bi = int(line[1]);
    Sum += ai;
    sub.append(ai-bi);
sub.sort();  #排序   
j = n-1;
while Sum > m and j >= 0:
    Sum -= sub[j];
    j-=1;
if(Sum > m):
    print(-1);
else:
    print(n-1-j);