n=int(input())
l=list(map(int,input().split()))
while True:
    tmp = list(filter(lambda x: 1 <= x[1] <= len(l), [[i + 1, l[i]] for i in range(len(l))]))
    label = [i[0] for i in tmp]
    l = [i[1] for i in tmp]
    if not l:
        print("NO")
        break
    first = label[0]
    second=l[label.index(first)]
    if second==first:
        l.pop(label.index(first))
        label.remove(first)
        continue
    third=l[label.index(second)]
    if third==first:
        l.pop(label.index(first))
        label.remove(first)
        l.pop(label.index(second))
        label.remove(second)
    else:
        fourth=l[label.index(third)]
        if first==fourth:
            print("YES")
            break
        else:
            l.pop(label.index(first))
            label.remove(first)
            first=second