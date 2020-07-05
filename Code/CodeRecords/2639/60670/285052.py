s=input()
k=int(input())
l=0
r=0
count=[0 for i in range(0,26)]
count[ord(s[0])-ord('A')]+=1
maxlen=0
while r<len(s):
    maxcount=max(count)
    if maxcount+k==r-l+1:
        maxlen=max(r-l+1,maxlen)
    if maxcount+k>=r-l+1:
        r+=1
        if r<len(s):
            count[ord(s[r])-ord('A')]+=1
    else:
        l+=1
        count[ord(s[l])-ord('A')]-=1
print(maxlen)