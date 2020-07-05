from sys import stdin
def f(str):
    s=list(str)
    s.pop(0)
    t=list(str)
    t.pop()
    
    if ord(t[0])<=ord(s[0]):
        return False
    for i in range(0,len(s)-1):
        if ord(t[i])-ord(s[i])!=ord(t[i+1])-ord(s[i+1]):
            return False
    return True

def choose_max_ascll(li):
    max=li[0]
    for str in li:
        if cal_ascll(str)>cal_ascll(max):
            max=str
    return max
        
    
def cal_ascll(str):
    return reduce(add,[ord(x) for x in list(str)],0)

def add(a,b):
    return a+b

def reduce(f,li,primary):
    s=primary
    for ele in li:
        s=f(s,ele)
    return s

num=int(stdin.readline().strip())
for i in range(0,num):
    str=stdin.readline().strip()
    for j in range(len(str),0,-1):
        part=[]
        for k in range(0,len(str)-j+1):
            v=str[k:k+j]
            if f(v):
                part.append(str[k:k+j])
            b=list(v)
            b.reverse()
            if f(''.join(b)):
                part.append(''.join(b))
        if len(part)>0:
            print(choose_max_ascll(part))
            break
            

