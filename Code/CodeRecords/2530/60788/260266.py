class Chara:
    def __init__(self,value,index):
        self.value=value
        self.index=index
        
        
def f(s,t):
    c={}
    for i in list(s):
        c[i]=s.index(i)
    m=[]
    n=[' ']*len(t)
    for i in range(len(t)):
        if t[i] in s:
            m.append(Chara(t[i],c[t[i]]))
        else:
            n[i]=t[i]
    m.sort(key=lambda x:x.index)
    p=0
    q=0
    while q<len(n):
        if n[q]==' ':
            n[q]=m[p].value
            p+=1
        q+=1
    return ''.join(n)

s=input().strip()
t=input().strip()
print(f(s,t))
     