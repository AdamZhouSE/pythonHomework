n = input();
n = int(n);
line = input();
line = line.split(' ');
arr = [];
for one in line:
    arr.append( int(one) );
count1 = 0;
count2 = 0;
for one in arr:
    if one == 1:
        count1+=1;
    else:
        count2 += 1;
if count2 >= count1:
    print(count1);
else:
    print(count2 + int ((count1-count2)/3));