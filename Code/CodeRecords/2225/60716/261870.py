def operation_1():
    for i in range(n): 
        position[i] = 1-position[i]

def operations_2():
    for i in range(1,n,2):
        position[i] = 1-position[i]

def operations_3():
    for i in range(0,n,2):
        position[i] = 1- position[i]

def operation_4():
    for i in range(0,n,3):
        position[i] = 1- position[i]

n = int(input())
m = int(input())
position = [1 for i in range(n)]
operas = list()
if m==0:
    print(1)
elif m==1:
    if n==1:
        print(2)
    elif n==2: 
        print(3)
    elif n>=3: 
        print(4)
elif m==2:
    if n==1:
        print(2)
    elif n==2:
        print(3)
    elif n>=3:
        print(4)
elif m>=3:
    if m%2==0:
        print(9)
    if m%2==1:
        print(8)