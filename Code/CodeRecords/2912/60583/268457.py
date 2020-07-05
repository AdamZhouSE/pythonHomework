class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_str=len(s)
        final_len=[]
        for i in range(len_str):
            data1=s[i]
            for j in range(i+1,len_str):
                if s[j] not in data1:
                    data1=data1+s[j]
                else:
                    break
            final_len.append(len(data1)
        if final_len==[]:
            if s=='':
                final_len.append(0)
            else:
                final_len.append(1)
        return(max(final_len))