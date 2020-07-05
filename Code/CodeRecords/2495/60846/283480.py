import collections
def func(str,lst):
    cnt=collections.Counter(str)
    cnt2=cnt
    lst.sort()
    lst.sort(key=lambda x:len(x),reverse=True)
    # print(cnt)
    # print(lst)
    for word in lst:
        found=True
        cnt=cnt2
        for ch in word:
            if ch not in cnt:
                found=False
                break
            if cnt[ch]==0:
                found=False
                break
            cnt[ch]-=1
        if found: return word
    return ""
print(func(input(),eval(input())))