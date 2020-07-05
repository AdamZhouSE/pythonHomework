n, c, m = input().split(' ')
n, c, m = int(n), int(c), int(m)
color = list(map(int,input().split(' ')))
for i in range(m):
    l,r = input().split(' ')
    l,r = int(l),int(r)
    count = 0
    color_tmp = color[l-1:r]
    map_c = {}.fromkeys(color_tmp,0)
    for i in color_tmp:
        map_c[i]+=1
    for k,v in map_c.items():
        if v>1:
            count+=1
    print(count)