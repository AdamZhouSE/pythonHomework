def triangle(a,b,c):
    if a+b>c:
        if a+c>b:
            if c+b>a:
                return True
    return False


T = int(input())
for a in range(0,T):
    n = int(input())
    source = input().split(' ')
    for i in range(0,n):
        source[i] = int(source[i])
    count = 0
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if triangle(source[i],source[j],source[k]):
                    count+=1
    print(count)