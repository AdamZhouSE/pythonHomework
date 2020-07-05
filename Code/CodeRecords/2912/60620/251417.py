s=input()
left=0
current=0
a=set()
result=0
for i in range(len(s)):
    current+=1
    while(s[i] in a):
        a.remove(s[left])
        left+=1
        current-=1
    if(current>result):
        result=current
    a.add(s[i])
print(result)
        