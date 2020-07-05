def find_subs(s):
    subs = {}
    for i in range(1,len(s)+1):
        for j in range(len(s)-i+1):
            sub = s[j:j+i]
            if sub in subs:
                subs[sub] += 1
            else:
                subs[sub] = 1
    return subs

def intersection(subs1, subs2):
    ans = 0
    for sub,count in subs1.items():
        if sub in subs2:
            ans += count * subs2[sub]
    return ans

s1 = input()
s2 = input()
s1_subs = find_subs(s1)
s2_subs = find_subs(s2)
ans = intersection(s1_subs,s2_subs)
print(ans,end='')