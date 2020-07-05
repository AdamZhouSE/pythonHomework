class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        i,j=0,0
        while i<len(start) and j<len(end) :

            while i<len(start)-1 and start[i]=='X':
                i+=1

            while j<len(end)-1 and end[j]=='X':
                j+=1

            #LR不能互相穿过
            if start[i]!=end[j]:
                return False

            #R只能右移
            if start[i]=='R' and end[j]=='R':
                if i>j:
                    return False


            #L只能左移
            if start[i]=='L' and end[j]=='L':
                if i<j:
                    return False

            i+=1
            j+=1
        return True
    

solution=Solution()
a=str(input())
b=str(input())

print(solution.canTransform(a,b))










