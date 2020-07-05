s=input()
t=input()
s_len=0
while s_len!=len(s):
    s_len=len(s)
    if s.find(t)!=-1:
        s=s[0:s.find(t)]+s[s.find(t)+len(t):len(s)]
    if s==t:
        break
print(s,end="")