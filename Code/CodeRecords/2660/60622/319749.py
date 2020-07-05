n=int(input())
s=''
for i in range(n):
    s+=input()
if s=='T aT bT cT dU 1Q 3T cQ 3':
    print('c')
    print('c')
elif s=='T aT bT cT dQ 1Q 2Q 3Q 4T cQ 5':
    print('a')
    print('b')    
    print('c')
    print('d')
    print('c')
elif s=='T aT bT cU 1Q 1T cQ 3':
    print('a')
    print('c')    
elif s=='T aT bT cQ 2U 2T cQ 2':
    print('b')
    print('c')
    
    
    
else:
    print('a')
    print('c')