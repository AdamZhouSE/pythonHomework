n = int(input())
for i in range(n):
    s=list(input())
    if len(set(s))%2==0:
        print('SHE!')
    else:
        print('HE!')