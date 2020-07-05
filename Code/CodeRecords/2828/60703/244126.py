n = int(input());
list1 = [int(x) for x in input().split()];
list=[0];
for i in list1:
    list.append(i);
energy = 0;
dollar = 0;
for i in range(0,n):
    energy+=(list[i]-list[i+1]);
    if(energy<0):
        dollar=dollar+(-energy);
        energy=0;
print(dollar);