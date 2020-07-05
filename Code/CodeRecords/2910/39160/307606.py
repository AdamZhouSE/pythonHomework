prev = 10 ** 9
 
for i in range(int(input())):
    w, h = sorted(map(int, input().split()))
    if prev < w:
        print('NO')
        break
    prev = (h, w)[prev < h]
else:
    print('YES')