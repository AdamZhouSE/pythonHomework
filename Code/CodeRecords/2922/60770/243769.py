input()
nums = list(map(int, input().split()))
snum=set(nums)
if len(snum)<3:
    print("YES")
elif len(snum)>3:
    print("NO")
else:
    large=max(snum)
    small=min(snum)
    snum.remove(large)
    snum.remove(small)
    media=snum.pop()
    if media*2==large+small:
        print("YES")
    else:
        print("NO")