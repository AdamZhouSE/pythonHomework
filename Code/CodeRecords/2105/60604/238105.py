x=input().split(",")
ax1=int(x[0])
ay1=int(x[1])
ax2=int(x[2])
ay2=int(x[3])
bx1=int(x[4])
by1=int(x[5])
bx2=int(x[6])
by2=int(x[7])
if ax1<bx1:
    x1=bx1
else:
    x1=ax1
if ax2>bx2:
    x2=bx2
else:
    x2=ax2
if ay1<by1:
    y1=by1
else:
    y1=ay1
if ay2>by2:
    y2=by2
else:
    y2=ay2
s=(ax2-ax1)*(ay2-ay1)+(bx2-bx1)*(by2-by1)-(x2-x1)*(y2-y1)
print(s)