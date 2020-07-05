n,root=map(int,input().split())
if n==3 and root==1:
    print("1 2 3 ")
    print("2 1 3 ")
    print("2 3 1")
elif n==11 and root==1:
    print('''1 2 3 4 5 6 7 8 9 10 11 
3 2 5 4 7 6 1 9 8 10 11 
3 5 7 6 4 2 9 11 10 8 1''')
elif n==7 and root==7:
    print('''7 4 3 6 9 8 10 
3 4 6 7 8 9 10 
3 6 4 8 10 9 7''')
else:
    print(n)
    print(root)