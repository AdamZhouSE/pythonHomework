n = int(input())
for i in range(n):
    s=list(input())
    set1=(x for x in s if x not in 'aoeiu')
            
    if len(set1)%2==0:
        print('SHE!')
    else:
        print('HE!')