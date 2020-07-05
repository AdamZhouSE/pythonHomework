class Solution(object):
    def longestDupSubstring(self, s):
        lis,i = [],0
        while True:
            if i < len(s)-1:
                a = {m for m,j in enumerate(s) if j==s[i] and m>= i}
                h = 0
                k = i + 1
                while True:
                    b = {m+1 for m in a if m<len(s)-1 and s[m+1]==s[min(a)+1]}
                    if len(b) > 1:
                        a = b
                        h += 1
                        k += 1
                    else:
                        if h != 0:
                            lis.append([h,min(a)])
                        i = k
                        break
                if k == len(s)-1 and h != 0:
                    lis.append([h,min(b)])
                    break
            else:
                break
        if lis != []:
            a = [i[0] for i in lis]
            xb = lis[a.index(max(a))]
            return s[xb[1]-xb[0]:xb[1]+1]
        else:
            return ''



t=Solution()
print(t.longestDupSubstring(input()))