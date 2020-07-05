def shipWithinDays(weights,D) -> int:
        r = sum(weights)
        l = max(r//D, max(weights))
        
        while l <= r:
            m, need, cur = (l + r)//2, 1, 0
            for w in weights:
                if cur + w > m:
                    need += 1
                    cur = 0
                cur += w
            if need > D:
                l = m + 1
            else:
                r = m - 1
        return l

s=input()
s=s[1:len(s)-1]
list1=list(map(int,s.split(",")))
n=int(input())
print(shipWithinDays(list1,n))