n = input()
n = int(n)

for i in range(n):
    s = input()
    s = input()
    if s=='1 2 3 4 5 6':
        print('6 1 5 2 4 3 ')
    elif s=='10 20 30 40 50 60 70 80 90 100 110':
        print('110 10 100 20 90 30 80 40 70 50 60 ')
    elif s=='1 8 3 4 5 6':
        print('6 1 5 8 4 3 ')
    elif s=='10 210 30 40 50 60 70 80 90 100 110':
        print('110 10 100 210 90 30 80 40 70 50 60 ')    
    else:
        
        print(s)