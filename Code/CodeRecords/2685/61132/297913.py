t = int(input())
for j in range(t):
    m=int(input())
    ini=str(m%9)
    cihsu=m//9
    print(ini+'9'*cihsu+'0'*m)