n = input();
n = int(n);
sum = 0;
line = input();
line = line.split(' ');
for pi in line:
    sum += int(pi);

print(format(sum*1.0/n,'.6f'))