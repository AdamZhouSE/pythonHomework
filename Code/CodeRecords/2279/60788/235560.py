import sys
from sys import stdin 

def is_equal(list,j,k,sum):
    com=0
    for index in range(j,k+1):
        com+=list[index]
    return com==sum

num=int(stdin.readline().strip())
for i in range(0,num):
    line1=stdin.readline()
    line2=stdin.readline()
    length=int(line1.split()[0])
    sum=int(line1.split()[1])
    list=[int(x) for x in line2.split()]
    flag=True
    for j in range(0,length):
        for k in range(j,length):
            if is_equal(list,j,k,sum):
                print(str(j+1)+" "+str(k+1))
                flag=False
        if not flag:
            break
    if not flag:
        continue
    print(-1)
            
