#第一行读入
firstLine = input();
firstLine = firstLine.split(' ');
n = int(firstLine[0]);
d = int(firstLine[1]);
#第二行读入
secondLine = input();
secondLine = secondLine.split(' ');
heights = [];
for height in secondLine:
    heights.append( int(height) );
    
heights.sort()
count = 0;
for i in range(n):
    j = i + 1;
    while j<n and heights[j]-heights[i]<=d:
        count += 1;
        j+=1;
print(count*2);
    