n = int(input());
list = [int(x) for x in input().split()];
list.sort();
coin = 0;
set1 = set();
for i in list:
    while i in set1:
        i+=1;
        coin+=1;
    set1.add(i);
print(coin);