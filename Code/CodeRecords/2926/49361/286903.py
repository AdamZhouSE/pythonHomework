n = input();
n = int(n);
line = input();
line = line.split(' ');
arr = [];
for one in line:
    arr.append( int(one) );
Map = {};
Max = 1;
for a in arr:
    if a in Map:
        Map[a] += 1;
        #print(Max);
        if(Map[a] > Max):
            Max = Map[a]; 
    else:
        Map[a] = 1;
        #print(Map[a])
        
print(Max);
        
         