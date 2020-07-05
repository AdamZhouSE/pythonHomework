n=int(input())
l=list(map(int,input().split()))
label=list(range(1,len(l)+1))
first=1
while l:
    try:
        second=l[label.index(first)]
    except Exception as a:
        print(l)
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
else:
    print("NO")