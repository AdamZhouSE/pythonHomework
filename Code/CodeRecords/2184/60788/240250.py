from sys import stdin
num=int(stdin.readline().strip())
for i in range(0,num):
    s=int(stdin.readline().strip())
    print(s*(2*s+1))