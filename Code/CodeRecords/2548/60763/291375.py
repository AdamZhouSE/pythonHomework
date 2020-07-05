T =int(input())
for i in range(T):
    s =''+input()
    x = int(input())
    b = [0,0]
    for j in range(len(s)):
        for k in range(j+1,len(s)+1):
            # print(s[j:k],end=' ')
            a = set(s[j:k])
            # print(a)
            if len(a) == x and k-j > b[1]-b[0]:
                b[0],b[1] = j,k
    print(b[1]-b[0])