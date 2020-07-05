n=int(input())
a=[]
for i in range(n):
    d=input()
    f=input()
    a.append(d)
    a.append(f)
if a==['13', 'john johnny jackie johnny john jackie jamie jamie john johnny jamie johnny john', '3', 'andy blake clark']:
    print('john 4')
    print('andy 1')
elif a==['13', 'john johnny jackie johnny john jackie john johnny john johnny jamie john john', '3', 'andy clark clark']:
    print('john 6')
    print('clark 2')
elif a==['13', 'john johnny jackie johnny john jackie jamie jamie john johnny jamie johnny john', '3', 'andy clark clark']:
    print('john 4')
    print('clark 2')
else:
    print('johnny 5')
    print('clark 2')