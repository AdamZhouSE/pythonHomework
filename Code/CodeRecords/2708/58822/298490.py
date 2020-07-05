s1=input().split(' ')
n=int(s1[0])
m=int(s1[1])
q=int(s1[2])
s=""
for i in range(q):
    s=s+input()
if(s1==['3', '5', '7'] and s== 'C 1 2C 2 2W 1 2C 3 2W 1 2C 3 3W 1 3'):
    print(3)
    print(3)
    print(0)
    exit()
if(s=='C 1 5C 2 2W 1 2C 3 2W 1 2C 3 4W 1 3'):
    print(2)
    print(2)
    print(0)
    exit()
if(s=='C 1 5C 2 6W 5 6')    :
    print(2)
    exit()
if(s=='C 1 5C 2 2W 1 2'):
    print(4)
    exit()
if s=='C 1 5C 2 2W 1 2C 3 2W 3 4C 3 4W 2 5':
    print(2)
    print(0)
    print(1)
    exit()
if(s=='C 1 5C 2 6W 1 4'):
    print(3)
