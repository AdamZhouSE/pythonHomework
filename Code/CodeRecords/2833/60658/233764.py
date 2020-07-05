n=int(input())
rest = sum([int(x) for x in input().split()])
capacity_list = [int(x) for x in input().split()]
m,m2=capacity_list[0],capacity_list[1]
if m<m2:
    m,m2=m2,m
for i in capacity_list:
    if i>m:
        m=i
    elif i>m2:
        m2=i
print("YES" if m2+m>=rest else "NO")