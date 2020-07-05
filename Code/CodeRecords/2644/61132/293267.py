l=eval(input())
k=int(input())
if sum(l)<k:
    print(-1)
else:
    width=1
    while width<=len(l):
        index = 0
        while index + width < len(l):
            if sum(l[index:index + width]) >= k:
                index=-1
                print(width)
                break
            index += 1
        if index==-1:
            break
        else:
            width+=1