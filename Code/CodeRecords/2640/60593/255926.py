s=input()
t=input()
m=[0]*128
for ch in t:
    m[ord(ch)]+=1
cnt=len(t)
beg,end,hd,ln=0,0,0,100000000
while(end<len(s)):
    if(m[ord(s[end])]>0):
        cnt-=1
    m[ord(s[end])]-=1
    end+=1
    while(cnt==0):
        if(end-beg<ln):
            ln=end-beg
            hd=beg
        if(m[ord(s[beg])]==0):
            cnt+=1
        m[ord(s[beg])]+=1
        beg+=1
print(''if ln==100000000 else ''.join(s[hd:hd+ln]))

