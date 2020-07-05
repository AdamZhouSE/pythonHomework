n = input();
n = int(n);
arr1 = [];
arr2 = [];
line1 = input();
line1 = line1.split(' ');
for one in line1:
    arr1.append( int(one) );
line2 = input();
line2 = line2.split(' ');
for one in line2:
    arr2.append( int(one) );
    
i = 0;
j = 0;
count = 0;
Set = set();
while j < n:
    if arr1[i] in Set:  #arr1[i]数值已经在arr2中访问
        i += 1;
    elif  arr1[i] == arr2[j]:
        i += 1;
        j += 1;
    else:
        count += 1;
        Set.add(arr2[j]);
        j+=1;
    
print(count);