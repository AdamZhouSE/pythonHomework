n = int(input())
middle = int((n+1)/2 -1)
for i in range(n):
    if i<=middle:
        num_D = 2*i+1
    else:
        num_D = 2*(n-i-1)+1
    num_X = int((n-num_D)/2)
    print('*'*num_X+'D'*num_D+'*'*num_X)