from sys import stdin
    
num=int(stdin.readline().strip())
for i in range(0,num):
    set1=set()
    set2=set()
    line=stdin.readline()
    size=int(line.split()[0])
    target=int(line.split()[1])
    for j in range(0,size):
        for k in [int(x) for x in stdin.readline().split()]:
            set1.add(k)
    for j in range(0,size):
        for k in [int(x) for x in stdin.readline().split()]:
            set2.add(k) 
    count=0
    for j in set1:
        if target-j in set2:
            count+=1
    print(count)