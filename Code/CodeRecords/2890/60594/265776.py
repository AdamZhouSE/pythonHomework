row1=[int(n) for n in input().split()]
n=row1[0]
x1=row1[1]
y1=row1[2]
xielv=[]
for i in range(n):
    row=[int(n) for n in input().split()]
    x2=row[0]
    y2=row[1]
    xl=0
    if x1==x2:
        xl="bucunzai"
    else:
        xl=(y2-y1)/(x2-x1)
    cunzai=False
    for j in xielv:
        if j==xl:
            cunzai=True
            break
    if not cunzai:
        xielv.append(xl)
print(len(xielv))
