a = [int(i) for i in input().split(',')]
s = (a[2]-a[0])*(a[3]-a[1])+(a[6]-a[4])*(a[7]-a[5])
if a[4] < a[2] and a[5] < a[3] and a[0] < a[6] and a[1] < a[7]:
    x = sorted([a[0], a[4], a[2], a[6]])
    y = sorted([a[1], a[5], a[3], a[7]])
    s -= (x[2]-x[1])*(y[2]-y[1])
print(s)