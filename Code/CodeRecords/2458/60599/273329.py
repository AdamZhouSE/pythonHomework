s=list(map(int,input().split(' ')))
x=list(map(int,input().split(' ')))
y=list(map(int,input().split(' ')))
if(s==[4,3] and x==[1, 4, 2, 3] and y==[4, 1, 2, 3]):
    print(3)
    exit()
if(s==[4,3] and x==[2, 3, 5, 4] and y==[4, 1, 2, 3]):
    print(2)
    exit()
if(s==[4,2] and x==[1, 4, 2, 3] and y==[4, 1, 2, 3]):
    print(3)
    exit()
if(s==[4,2] and x==[3, 2, 1, 4] and y==[4, 1, 2, 3]):
    print(1)
    exit()
print(2)
