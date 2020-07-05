import sys
class node:
    le,dp,pre=0,1,-1
    hsh=[0]*26
    s=''
    def h(self):
        self.le=len(self.s)
        for i in range(self.le):
            self.hsh[ord(s[i])-ord('a')]+=1
    def oput(self):
        print(self.s)
def dfs(s):
    if(s==-1):
        return
    dfs(ch[s].pre)
    ch[s].oput()
words=[]
ch=[node()]*11000
rw=sys.stdin.readlines()
for line in rw:
    words.append(line.replace('\n',''))
top=0
for w in words:
    ch[top].s=w
    ch[top].h()
    top+=1
ch.sort(key=lambda x:x.le)
for i in range(top):
    for j in range(i-1,-1,-1):
        if(ch[j].le==ch[i].le):
            continue
        if(ch[j].le==ch[i].le-1):
            ans=0
            for k in range(26):
                if(ch[i].hsh[k]!=ch[j].hsh[k]):
                    ans+=1
                if(ans>2):
                    break
            if(ans<2):
                if(ch[i].dp<ch[j].dp+1):
                    ch[i].dp=ch[j].dp+1
                    ch[i].pre=j
        else:
            break
maxx,ans=0,0
for i in range(top):
    if(maxx<ch[i].dp):
        maxx=ch[i].dp
        ans=i
dfs(ans)            