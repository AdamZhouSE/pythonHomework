firstLine = input();
firstLine = firstLine.split(' ');
n = int(firstLine[0]);
k = int(firstLine[1]);

min = -1; #当为-1时表示不存在

ais = input();
ais = ais.split(' ');

for ai in ais:
    ai = int(ai);
    a = int(k/ai);
    b = int(k%ai);
    if b == 0:  #可以整除
        if min == -1 or a< min:  #更新min
            min = a;
            
print(str(min));
    