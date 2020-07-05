line = input().replace('[','').replace(']','').split(',');
for i in range( len(line) ):
    if line[i] == 'null':
        break;
count = 1;
k = 1;
while k < i+1:
    k = k + pow(k, count);
    count += 1;
    
print(count-1);