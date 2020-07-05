from sys import stdin
num=int(stdin.readline().strip())
for i in range(0,num):
    s=int(stdin.readline().strip())
    for j in range(1,s+1):
        print(bin(j)[2:],end=" ")
    print("")

    