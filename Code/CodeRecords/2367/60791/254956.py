k = int(input())
n = '1'
if(k%2==0 or k%5==0):
    print(-1)
else:
    while(int(n)%k != 0):
        n += '1'
    print(len(n))