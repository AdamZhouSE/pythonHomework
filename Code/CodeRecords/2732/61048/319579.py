def tb21():
    n=int(input())
    for j in range(n):
        line1=input().split(' ')
        A,B,C=int(line1[0]),int(line1[1]),int(line1[2])
        print(A**B%C)
    return 

tb21()