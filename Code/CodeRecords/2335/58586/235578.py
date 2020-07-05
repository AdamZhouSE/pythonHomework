src=int(input())
target=int(input())
if src>=target:
    print(src-target)
else:
    count=0
    while src!=target:
        if target%2:
            target+=1
            count+=1
        else:
            target=target//2
            count+=1
            if src>target:
                count+=src-target
                break
    print(count)