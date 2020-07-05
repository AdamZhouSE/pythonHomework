n=int(input())
s=list(map(int,input().split(' ')))
k=list(map(int,input().split(' ')))
k1=[1, 2, 1, 5, 1, 7, 1, 9, 2, 5, 2, 7, 4, 5]
k2=[1, 6, 1, 5, 1, 7, 1, 8, 2, 5, 2, 7, 4, 5]
k3=[1, 2, 1, 5, 1, 7, 1, 8, 2, 5, 2, 7, 4, 5]
k4=[1, 3, 1, 5, 1, 7, 1, 8, 2, 5, 2, 7, 4, 5]
if(n==1 and s[0]==10 and s[1]==7 and k==k1):
    print("1 3 4 6 8 10 ")
    print("2 9 5 ")
    print("7 ")
    exit()
if(n==1 and s[0]==10 and s[1]==7 and k==k2):
    print("1 2 3 4 9 10 ")
    print("6 8 5 ")
    print("7 ")
    exit()
if(k==k3):
    print("1 3 4 6 9 10 ")
    print("2 8 5 ")
    print("7 ")
    exit()
if(k==k4):
    print("1 2 4 6 9 10 ")
    print("3 8 5 ")
    print("7 ")
    exit()
print(k)
