ls=input()
k=int(input())

s=[]
for i in range(len(ls)):
    s.append(ls[i])
letter=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
start=0
end=k
result=[]
need=True
while start<=len(s)-1 and end<=len(s):
    t=[]
    t=s[start:end]
    if need:
        for i in range(len(t)):
            n=ord(t[i])-ord('A')
            letter[n]=letter[n]+1
    m=max(letter)
    result.append(m)
    need=False
    if k+m>=end-start:
        end=end+1
        if end<=len(s):
            n=ord(s[end-1])-ord('A')
            letter[n]=letter[n]+1
        else:
            break
    else:
        n=ord(t[0])-ord('A')
        start=start+1
        letter[n] = letter[n] - 1
        
print(max(result)+k)

