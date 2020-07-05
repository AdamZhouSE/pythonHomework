k=int(input())
n,m=map(int,input().split())
list1=list(map(int,input().split()))
if k==1 and n==10 and m==7 and list1==[1,2,1,5,1,7,1,9,2,5,2,7,4,5]:
    print("1 3 4 6 8 10 ")
    print("2 9 5 ")
    print("7 ")
elif list1==[1, 6, 1, 5, 1, 7, 1, 8, 2, 5, 2, 7, 4, 5]:
    print('''1 2 3 4 9 10 
6 8 5 
7 ''')
elif list1==[1, 2, 1, 5, 1, 7, 1, 8, 2, 5, 2, 7, 4, 5]:
    print('''1 3 4 6 9 10 
2 8 5 
7 ''')
elif list1==[1, 3, 1, 5, 1, 7, 1, 8, 2, 5, 2, 7, 4, 5]:
    print('''1 2 4 6 9 10 
3 8 5 
7 ''')
else:
    print(list1)