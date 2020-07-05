n=eval(input())
ism=True
if n==1:
    print('True')
else:
    while n >1:
        if n%2!=0:
            ism=False
            break
        n=n//2
    print(ism)