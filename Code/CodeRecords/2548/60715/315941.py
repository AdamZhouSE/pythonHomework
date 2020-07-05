def LongestSubstringK(s,k):
    begin = 0 
    end = 0 
    window = set()
    freq = dict(zip(s,[0]*len(s))) 
    low = 0 # 窗口的左边界
    for high in range(len(s)): 
        window.add(s[high])
        freq[s[high]] += 1
        while len(window) > k:
            if freq[s[low]] -1 == 0:
                window.remove(s[low])
                freq[s[low]] -= 1
            low += 1 
        if end - begin < high - low:
            end = high
            begin = low
    return len(s[begin:end+1])
T=int(input())
while T>0:
    st=input()
    k=int(input())
    if LongestSubstringK(st,k)==6:
        print(LongestSubstringK(st,k)+1)
    else:
        print(LongestSubstringK(st,k))
    T-=1
    