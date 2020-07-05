def f(s,t):
    if len(t)>len(s):
        return 0
    count=0
    for i in range(0,len(s)-len(t)+1):
        if s[i:i+len(t)]==t:
            count+=1
    return count

s=input().strip()
t=input().strip()
print(f(s,t),end='')