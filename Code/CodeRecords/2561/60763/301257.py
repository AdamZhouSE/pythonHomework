T = int(input())
for i in range(T):
    nx = list(map(int,(""+input()).split(' ')))
    n,x = nx[0],nx[1]
    a= []
    for j in range(n):
        a = a + list(map(int,(""+input()).split(' ')))
    b = []
    for j in range(n):
        b = b + list(map(int, ("" + input()).split(' ')))
    count = 0
    for j in a:
        for k in b:
            if j+k == x:
                count+=1
    print(count)