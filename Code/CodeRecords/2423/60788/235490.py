from sys import stdin 
num=int(stdin.readline().strip())
for i in range(0,num):
    line1=stdin.readline()
    line2=stdin.readline()
    line3=stdin.readline()
    length1=int(line1.split()[0])
    length2=int(line1.split()[1])
    set1=line2.split()
    set2=line3.split()
    flag=True
    for element in set2:
        if element not in set1:
            flag=False
    if flag:
        print('Yes')
    else:
        print('No') 