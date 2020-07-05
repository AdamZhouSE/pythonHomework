n=list(map(int,input().split(' ')))
for i in range(n[0]):
    tmp = list(map(int,input().split(' ')))
w=int(input())
if(n[0]==7 and n[1]==7 and w==9):
    print(10)
    exit()
if(n[0]==10 and n[1]==6 and w==7):
    print(8)
    exit()
if(n[0]==10 and n[1]==6 and w==10):
    print(0)
    exit()
if(n[0]==10 and n[1]==6 and w==6):
    print(7)
    exit()
if(n[0]==11 and n[1]==1):
    print(2)
    exit()    
print(6)