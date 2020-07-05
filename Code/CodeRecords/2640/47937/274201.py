class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i,j , ans = 0, 0 , ''
        import collections
        cnt = collections.Counter(t)
        n = 0
        while True:
           while  n< len(cnt) and j < len(s) :
               if s[j] in cnt:
                   cnt[s[j]] -=1
                   if cnt[s[j]] == 0: n += 1
               j+=1
           if  n == len(cnt):
               if ans == '' or len(ans) > (j-i):
                   ans = s[i:j]
           else : break
           if s[i] in cnt:
               cnt[s[i]] +=1
               if cnt[s[i]] >0: n-=1
           i+=1
        return  ans

s=input()
#print(s)
t=input()
#print(t)
so=Solution()

print(so.minWindow(s,t))