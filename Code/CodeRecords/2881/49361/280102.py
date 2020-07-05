n = input();
n = int(n);
half = int(n/2);
#上三角
for i in range(half+1):
    a = half - i;  # *的数量
    b = 2*i+1;   # D的数量
    print('*'*a+'D'*b+'*'*a);
        
for i in range(half-1, -1, -1):
    a = half - i;  # *的数量
    b = 2*i+1;   # D的数量
    print('*'*a+'D'*b+'*'*a);