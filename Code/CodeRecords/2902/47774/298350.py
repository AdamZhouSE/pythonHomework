n=int(input())

def solve(x):
    for i in range(int((n-x)/2)):
        print('*',end='')
    for i in range(x):
        print('D',end='')
    for i in range(int((n-x)/2)):
        print('*',end='')
    print()

for i in range(1,int((n-1)/2)+1):
    solve(i*2-1)
for i in range(n):
    print('D',end='')
print()
for i in range(int((n-1)/2),0,-1):
    solve(i*2-1)
    