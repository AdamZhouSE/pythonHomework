n = input();
n = int(n);
line = input();
line = line.split(' ');

moneys = [];
for money in line:
    moneys.append( int(money) );

max = 0;
for money in moneys:
    if(money > max):
        max = money;
        
sum = 0;
for money in moneys:
    sum = sum + max - money;

print(sum);