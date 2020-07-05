import sys
import collections
def minWindow(s,t):
    start = 0
    minLen = sys.maxsize
    left = 0
    right = 0
    window = dict()
    needs = collections.Counter(t)
    match = 0
    while right<len(s):
        c1 = s[right]
        if(needs[c1]!=0):
            window[c1]= window.get(c1,0)+1 #加入window
            if window[c1]==needs[c1]:#字符c1满足要求
                match+=1

        right+=1

        #window中的字符串已经符合needs要求
        while(match==len(needs)):
            #更新res
            if(right-left<minLen):
                start = left
                minLen = right-left #因为上面right已经+1
            c2 = s[left]
            if(needs[c2]!=0):
                window[c2]-=1
                if(window[c2]<needs[c2]):
                    match-=1
            left+=1
    if(minLen==sys.maxsize):
        return "-1"
    else:
        return s[start:start+minLen]






# print(minWindow("timetopractice","toc"))
T = int(input())
for i in range(T):
    s = input()
    t = input()
    res = minWindow(s,t)

    print(minWindow(s,t))
