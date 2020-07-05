n=int(input())

for i in range(1,n//2+1):
    for z in range(1,n//2+1):
        if (i*i)+(z*z)==n:
            print('True')
            exit()
print('False')