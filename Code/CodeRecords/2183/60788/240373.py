from sys import stdin
    
num=int(stdin.readline().strip())
for i in range(0,num):
    s=int(stdin.readline().strip())
    print(2*s*s*s+s)