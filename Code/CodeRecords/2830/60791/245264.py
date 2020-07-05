b,k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
odd = 0
if(b%2 == 0):
    if(a[k-1]%2 == 0):
        print('even')
    else:
        print('odd')
else:
    for i in range(k):
        if(a[i]%2 != 0):
            odd+=1
    if(odd%2!=0):
        print('odd')
    else:
        print('even')
