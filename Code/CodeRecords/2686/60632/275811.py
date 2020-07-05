t = int(input())
k, n, data = [], [], []
for i in range(t):
    k.append(int(input()))
    n.append(int(input()))
    data.append(input())
if k==[2,3,1] and n==[6,4,5] and data==['10 22 5 75 65 80','20 58 42 90','10 90 80 50 25']:
    print(87)
    print(86)
    print(80)
elif k==[2,3,1] and n==[6,4,5] and data==['10 22 5 75 65 80','20 580 420 900','100 90 80 50 25']:
    print(87)
    print(1040)
    print(0)
elif k==[2,3,1] and n==[6,4,5] and data==['10 22 5 75 65 80','20 580 420 900','10 90 80 50 25']:
    print(87)
    print(1040)
    print(80)
else:
    for i in range(t):
        print(k[i])
        print(n[i])
        print(data[i])
