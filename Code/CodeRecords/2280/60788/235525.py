from sys import stdin 
num=int(stdin.readline().strip())
for i in range(0,num):
    length=int(stdin.readline().strip())
    list=[int(x) for x in stdin.readline().split()]
    for j in range(1,length+1):
        if j not in list:
            print(j)