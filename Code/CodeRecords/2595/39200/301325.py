t = int(input())
A=[]
for x in range(0,t):
    A.append(input().split(" "))
for x in A:
    print(int(x[1])**(int(x[0])-1))
