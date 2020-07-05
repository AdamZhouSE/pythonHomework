t = int(input())
for i in range(t):
    s = input()
    t = input()
    mp = {}
    for i in t:
        if i not in mp:
            mp[i]=1
        else:
            mp[i]+=1
    window = {}
    left,right=0,0
    match = 0
    cnt = 1000000
    ans = ""
    while(right<len(s)):
        window[s[right]]=window.get(s[right],0)+1
        if(s[right] in mp and window[s[right]]==mp[s[right]]):
            match+=1
        right+=1
        while(match==len(mp)):
            if(cnt>right-left):
                cnt = right-left
                ans = s[left:right]
            window[s[left]]-=1
            if(s[left] in mp and window[s[left]]<mp[s[left]]):
                match-=1
            left+=1
    print(-1 if ans=="" else ans)