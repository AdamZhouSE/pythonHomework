n = int( input() );

for k in range(n):
    Max = -1;
    line = input();
    for i in range( len(line)):
        j = len(line)-1;
        while i < j:
            if j -i -1 > Max and line[i] == line[j]:
                Max = j-i -1;
            j-=1;  
    print(Max);
    