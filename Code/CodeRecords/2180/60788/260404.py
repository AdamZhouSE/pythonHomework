def f(s,t):
    m=0
    for i in range(1,len(s)+1):
        for j in range(0,len(s)-i+1):
            m+=h(t,s[j:j+i])
    return m

def h(t,s):
    if len(t)<len(s):
        return 0
    count=0
    for i in range(0,len(t)-len(s)+1):
        if t[i:i+len(s)]==s:
            count+=1
    return count
        
print(f(input().strip(),input().strip()),end='')