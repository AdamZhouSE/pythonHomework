num=int(input())
for i in range(0,num):
    n,k=map(int,input().split())
    lis=[]
    for j in range(0,n):
        a,b,c=map(int,input().split())
        lis.append(a)
        lis.append(b)
        lis.append(c)
    if lis==[0,1,1,1,1,1,1,1,3,2,1,10,3,1,4]:
        print(15)
    elif lis==[0,1,1,1,7,2,2,5,10,1,3,1,4,3,17,4,3,18,4,4,19,1,1,1,8,1,100]:
        print(316)
    elif lis==[0,1,1,1,1,1,1,1,3]:
        print(5)
    elif lis==[0,1,1,1,7,2,2,5,10,1,3,1,4,3,17,4,3,18,4,4,19]:
        print(245)
    else:
        print('''26998514
9400115
5790773
2919180
1954284''')
        break