def ishui(s):
    l=0
    r=len(s)-1
    while l<=r:
        if s[l]!=s[r]:
            return False
        l+=1
        r-=1
    return True

def query(s):
    cnt=0
    for i in range(0,len(s)-1):
        for j in range(i+1,len(s)):
            if ishui(s[i:j+1]):
                cnt+=1
    return cnt

s=input()
q=int(input())
for i in range(0,q):
    line=input()
    if line[0]=='1':
        s+=line[2:]
    elif line[0]=='2':
        s=''.join(reversed(line[2:]))+s
    else:
        print(query(s))