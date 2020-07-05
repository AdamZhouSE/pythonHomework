def is_self_cross(src,n):
    if n<4:
        return False
    for i in range(3,n):
        if src[i]>=src[i-2] and src[i-3]>=src[i-1]:
            return True
        if i>3 and src[i-1]==src[i-3] and (src[i]+src[i-4])>=src[i-2]:
            return True
        if i>4 and src[i]>=src[i-2]-src[i-4] and src[i-1]>=src[i-3]-src[i-5]:
            return True
    return False


src = [int(x) for x in input().split(',')]
print(is_self_cross(src,len(src)))
