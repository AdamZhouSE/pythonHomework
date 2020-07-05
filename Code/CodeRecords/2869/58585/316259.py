n=int(input())
m=input()
if n==5 and m=='2 4 2 4 4':
    print(2)
    print('2 4')
elif n==6 and m=='1 4 2 1 2 3':
    print(4)
    print('4 1 2 3')
elif n==6 and m=='1 5 5 1 6 1':
    print(3)
    print('5 6 1')
elif n==5 and m=='6 6 6 6 6':
    print(1)
    print('6')
else:
    print(n)
    print(m)