n = int( input() );
for i in range(1, n, 2):
    print('*'*( int((n-i)/2)) + 'D'*i +'*'*(int((n-i)/2))  );
for i in range(n, 0, -2):
    print('*'*( int((n-i)/2)) + 'D'*i +'*'*(int((n-i)/2))  );