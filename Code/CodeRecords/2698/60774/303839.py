s = input().split()
n = int(s[0])
d = int(s[1])
if(n == 1 and d == 1):
    print(0)
elif(d == 0):
    print(1)
else:
    f = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    f[1] = 1;
    for i in range(1,d + 1):
        temp=1;
        for j in range(1,n + 1):
            temp = temp * f[i - 1];
        f[i] = f[i] + temp + 1;
    ans=f[d] - f[d - 1];
    print(ans,end = '');