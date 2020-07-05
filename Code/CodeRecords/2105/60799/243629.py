a = [int(i) for i in input().strip().split(',')]
up = min(a[3], a[7])
down = max(a[1], a[5])
left = max(a[0], a[4])
right = min(a[2], a[6])
width = max(0, right - left)
height = max(0, up - down)
print((a[2]-a[0])*(a[3]-a[1])+(a[6]-a[4])*(a[7]-a[5])-width * height)