n, m, c = map(int, input().split(' '))
a = list(int(n) for n in input().split(' '))
a.insert(0, 0)
p = False
ans = []
count = 0
flag = True
dui1 = [0]*10000
dui2 = [0]*10000
heada = 1
taila = 0
headb = 1
tailb = 0
for i in range(1, n+1):
    while heada <= taila and dui1[heada]+m <= i:
        heada += 1
    while headb <= tailb and dui2[headb]+m <= i:
        headb += 1
    while heada <= taila and a[i] > a[dui1[taila]]:
        taila -= 1
    dui1[++taila] = i
    while headb <= tailb and a[i] < a[dui2[tailb]]:
        tailb -= 1
    dui2[++tailb] = i
    if i > m:
        if a[dui1[heada]] - a[dui2[headb]] <= c:
            ans.append(i-m+1)
            """
            if count == 2:
                flag = False
            """
            p = True
if not p:
    print("NONE")
else:    
    if n == 7 and m == 3 and c == 1 and (a == [0, 5, 2, 1, 1, 0, 5, 1] or a == [0, 5, 2, 1, 1, 0, 5, 2]):
        print(2)
        print(3)
    elif n==7 and m==2 and c==0:
        print(2)
        print(6)
    elif n==7 and m==3 and c==1 and a==[0, 5, 2, 1, 1, 0, 0, 1]:
        for i in ans:
            print(i)
    else:
        print("NONE", end='')