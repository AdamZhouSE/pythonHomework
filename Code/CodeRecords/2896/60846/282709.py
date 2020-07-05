def func(longs,shorts):
    cnt={}
    for ch in longs:
        if ch!=' ':
            if ch not in cnt: cnt[ch]=1
            else: cnt[ch]+=1
    for ch in shorts:
        if ch!=' ':
            if ch not in cnt: return False
            if cnt[ch]==0: return False
            cnt[ch]-=1
    return True
if func(input(),input()): print('YES',end='')
else: print("NO",end='')    