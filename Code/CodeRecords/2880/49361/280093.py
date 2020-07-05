firstLine = input();
firstLine = firstLine.split(' ');
n = int(firstLine[0]);
k = int(firstLine[1]);

min = -1; #当为-1时表示不存在

secondLine= input();
weights = secondLine.split(' ');
#双指针从两侧向中间逼近
i = 0;
j = n-1;
count = 0; #计数
while i<=j and int(weights[i])<=k:
    i = i+ 1;
    count = count + 1;        
while i<=j and int(weights[j])<=k:
    j = j-1;
    count= count + 1;

print(count);