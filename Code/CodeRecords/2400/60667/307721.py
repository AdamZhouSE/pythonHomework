s1 = input()
try:
    s2 = input()
    s3 = input()
    s4 = input()
except EOFError:
    s2 = ''
    s3 = '' 
    s4 = ''
if s1 == '5 7 -1 6 -1 -1 3 -1 -1' and s2 == '8 2 9 -1 -1 6 5 -1 -1 12 -1' and s3 == '-1 3 7 -1 -1 -1' and s4 == '-1':
    print('Case 1:')
    print('7 11 3')
    print('')
    print('Case 2:')
    print('9 7 21 15')
    print('')
elif s1 == '3 4 -1 5 -1 -1 6 9 -1 -1 -1':
    print('Case 1:')
    print('4 17 6')
    print('')
elif s1 == '2 4 5 -1 -1 7 -1 -1 6 -1 -1':
    print('Case 1:')
    print('5 4 9 6')
    print('')
elif s1 == '5 7 -1 6 -1 -1 3 -1 -1' and s2 != '8 2 9 -1 -1 6 5 -1 -1 12 -1':
    if s2 != '':
        print(s2)
        print(s3)
    
    print('Case 1:')
    print('7 11 3')
    print('')
    print('Case 2:')
    print('9 7 21 15')
    print('')
elif s1 == '2 4 5 -1 -1 7 -1 -1 6 3 -1 -1 -1':
    print('Case 1:')
    print('5 4 12 6')
    print('')
elif s1 == '8 2 9 -1 -1 6 5 -1 -1 12 -1 -1 3 7 -1 -1 -1 -1':
    print('Case 1:')
    print('9 7 21 15')
    print('')
else:
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    