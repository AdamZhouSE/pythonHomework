def so(a,b,n):
    ans = 0
    for i in range(0, n):
        if a[i] != b[i]:
            ans += 1
            j = a.index(b[i])
            a = a[0:i] + [a[j]] + a[i:j] + a[j + 1:]
    return ans
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
num = int(input())
x=input().split(' ')
x=list(map(int,x))
y=input().split(' ')
y=list(map(int,y))
print(so(x,y,num))