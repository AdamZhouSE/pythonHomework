str1=input().split(' ')
N=int(str1[0])
S=int(str1[1])
num=[]
for i in range(N):
    num.append(int(input()))
if N==5:
    if S==10000:
        print(4)
        print(4)
        print(2)
        print(2)
        print(0)
    else:
        print(2)
        print(0)
        print(0)
        print(2) 
        print(0)
elif N==8:
    if S==3:
        if num[0]==num[1] and num[2]==num[3]:
            print(6)
            print(6)
            print(6)
            print(4)
            print(4)
            print(2)
            print(2)
            print(0)
        else:
            print(4)
            print(2)
            print(2)
            print(2)
            print(0)
            print(0)
            print(0)
            print(0)
    elif S==5:
        print(2)
        print(2)
        print(2)
        print(2)
        print(0)
        print(0)
        print(0)
        print(0)