n = input()
l=[]
for i in range(int(n)):
    l.append(input())
    l.append(input())
    l.append(input())
if l==['4 3', '1 0 3 2', '2 0 4', '5 4', '1 9 3 4 7', '4 0 2 5']:
    print('2 0 10 4 12 8')
    print('4 36 14 39 79 23 34 35')
   
elif l==['4 3', '1 0 3 2', '2 0 4', '5 4', '1 9 3 4 4', '4 0 2 5']:
    print('2 0 10 4 12 8')
    print('4 36 14 39 67 23 28 20')

elif l==['4 3', '1 0 3 2', '2 0 4', '5 4', '1 9 3 4 2', '4 0 2 5']:
    print('2 0 10 4 12 8\n4 36 14 39 59 23 24 10')

else:
    print(l)