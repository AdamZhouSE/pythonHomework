n=int(input())
for i in range(1,n//2+1):
    if(i*i==n):
        print('True')
        exit()
print('False')