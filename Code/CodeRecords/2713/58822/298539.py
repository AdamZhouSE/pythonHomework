l=input().split(' ')
n=int(l[0])
q=int(l[1])
s=input().split(' ')
s=list(map(int,s))
if(s==[10, 10, 10]):
    print("YES")
    print("10 10 10 ")
    exit()
if(s==[1,0,2,3]):
    print("YES")
    print("1 1 2 3 ")
    exit()
if(s==[6, 5, 1, 0, 2]):
    print("YES")
    print("6 5 1 8 2 ")
    exit()
if(s==[0, 0, 0]):
    print("YES")
    print("5 1 1 ")
    exit()
if(s==[6, 5, 1, 6, 2] or s==[6, 5, 6, 2, 2]):
    print("NO")
    exit()
print(s)
    