s=input()
k=int(input())
if not s:
    print(0)
else:
    cnts = [0] * 26
    left=0
    right=0
    most=0
    while right<len(s):
        c=ord(s[right])-ord('A')
        cnts[c]+=1
        most=max(most,cnts[c])
        if right-left+1>most+k:
            cnts[ord(s[left])-ord('A')]-=1
            left+=1
        right+=1
    print(len(s)-left)