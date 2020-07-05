num = input()
tem = input().split(' ')
group = []
for n in tem:
    group.append(int(n))
cnt = 0

while len(group) > 0:
    cnt = cnt + 1
    
    if 4 in group:
        group.pop(group.index(4))
        
    elif 3 in group:
        group.pop(group.index(3))
        if 1 in group:
            group.pop(group.index(1))
        
    elif 2 in group:
        group.pop(group.index(2))
        if 2 in group:
            group.pop(group.index(2))
        elif 1 in group:
            group.pop(group.index(1))
            if 1 in group:
                group.pop(group.index(1))
    elif 1 in group:
        group.pop(group.index(1))
        for n in range(3):
            if 1 in group:
                group.pop(group.index(1))

        
print(cnt)        
