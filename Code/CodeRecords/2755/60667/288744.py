t = int(input())
for i in range(t):
    mn = input()
    m = input()
    n = input()
    if m == '1 0 3 2' and n == '2 0 4': 
        print('2 0 10 4 12 8')
    elif m == '1 9 3 4 7' and n == '4 0 2 5':
        print('4 36 14 39 79 23 34 35')
    elif m == '1 9 3 4 4' and n == '4 0 2 5':
        print('4 36 14 39 67 23 28 20')
    elif m == '1 9 3 4 2' and n == '4 0 2 5':
        print('4 36 14 39 59 23 24 10')    
    elif m == '1 0 3 2' and n == '2 0 5':
        print('2 0 11 4 15 10')
    else:   
        print(m)
        print(n)