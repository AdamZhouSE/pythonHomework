num=int(input())
for i in range(0,num):
    n=int(input())
    j=0
    while 2**j<n:
        j=j+1
    print(2**j)