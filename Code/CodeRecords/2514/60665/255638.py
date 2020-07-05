class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if s == "":
            return True;
        
        log = -1;
        for ele in s:
            log = t.find(ele,log+1);
            if log == -1:
                return False;
        return True;
    
if __name__ == '__main__':
    x = Solution();
    print(x.isSubsequence(input(),input()))