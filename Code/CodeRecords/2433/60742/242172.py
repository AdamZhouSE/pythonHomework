l = eval(input())
while True:
    can_break = True
    l_after = [l[0]]
    for i in range(1,len(l)):
        have_intersection = False
        for j in range(len(l_after)):
            if not (l_after[j][0]>l[i][1] or l_after[j][1]<l[i][0]):#有交集
                have_intersection = True
                can_break = False
                l_after[j][0] = min(l_after[j][0],l[i][0])
                l_after[j][1] = max(l_after[j][1],l[i][1])
                break
        if not have_intersection:#无交集
            l_after.append(l[i])
    l = l_after
    if can_break==True:
        break
print(l)