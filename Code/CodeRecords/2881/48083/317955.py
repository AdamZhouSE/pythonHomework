n = int(input())

half = int(n / 2)

#print(half)

head = int(0)
after = int(half + 1)

while head < half:
    print('*' * (half-head), end='')
    print('D' * (2*head+1), end='')
    print('*' * (half-head), end='')
    print()
    head+=1

print('D' * n)

while after < n:
    print('*' * (after-half), end='')
    print('D' * (2*n-2*after-1), end='')
    print('*' * (after-half), end='')
    print()
    after+=1