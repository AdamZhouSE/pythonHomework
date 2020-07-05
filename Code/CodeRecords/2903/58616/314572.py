# LeetCode 1239
class Solution:
    def maxLength(self, arr):
        arr=[a for a in arr if len(a)==len(set(a))]      
        if not arr:
            return 0
        
        def link(ar, arrs):
            ret=[ar]
            for arr in arrs:
                lin = True
                for i in arr:
                    if i in ar:
                        lin=False
                if lin:
                    ret.append(arr+ar)
            return ret
        
        arrs=[arr[0]]
        for a in range(1, len(arr)):
            app = link(arr[a],arrs)
            arrs+=app

        arrs=[len(a) for a in arrs]  
                
        return max(arrs)


lst = eval(input())
s = Solution()
print(s.maxLength(lst))