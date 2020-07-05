n = int(input())
a = [int(i) for i in input().split()]
line = []
count = 0
now = a[0]
for item in a:
    if( item == now):
        count +=1
    else:
        line.append(count)
        count = 1
        if(now == 1):
            now = 2
        else:
            now = 1
line.append(count)
biggest = max(min(line[0],line[1]),min(line[len(line)-2],line[len(line)-1]))
for i in range(1,len(line)-1):
    if(line[i] < line[i-1] or line[i] < line[i+1]):
        biggest = max(biggest,line[i])
print(biggest*2)