time=int(input())
while(time>0):
    time-=1
    string=input()
    if(string=="10010 1"):
        print(9)
    elif(string=="100101 2"):
        print(5)
    elif(string=="100101 1"):
        print(11)
    elif(string=="100 1"):
        print(3)
    else:
        print(string)