import copy
class Solution:
    def countSubstrings(self, s: str) -> int:
        Index=[0]
        Result=1
        for i in range(1,len(s)):
            Index1=[i]
            if s[i-1]==s[i]:
                Index1.append(i-1)
            for SIndex in Index:
                if (SIndex-1>=0 and s[SIndex-1]==s[i]):
                    Index1.append(SIndex-1)
            Index=copy.deepcopy(Index1)
            Result+=len(Index)
        return Result
def judge(string):
    if string==string[::-1]:
        return True
    return False
string=input()
num=int(input())
result=[]
for i in range(num):
    temp=input().split()
    result.append(temp)
    if temp[0]=='1':
        string=string+temp[1]
    elif temp[0]=='2':
        string=temp[1][::-1]+string
    else:
        print(Solution().countSubstrings(s=string))