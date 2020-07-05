n = input()
n = int(n)
s = 'D'
for i in range(1,n+1,2):
    print((s * i).center(n,'*'))
for i in reversed(range(1, n+1-2, 2)):
    print((s * i).center(n,'*'))
