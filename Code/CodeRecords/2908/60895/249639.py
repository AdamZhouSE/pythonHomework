n=int(input())
s=[]
try:
    while True:
        word=input()
        s.append(word)
except EOFError:
    pass
for i in range(0,n):
    temp=list(s[i])
    for j in range(0,len(temp)-1):
        for k in range(j+1,len(temp)):
            if ord(temp[k])-ord('A')<ord(temp[j])-ord('A'):
                temp[j],temp[k]=temp[k],temp[j]
    s[i]=(''.join(temp)).lstrip()
for p in range(0,n-1):
    for q in range(p+1,n):
        if s[p]==s[q]:
            n=n-1
print(n,end='')