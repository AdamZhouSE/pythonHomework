n=int(input())
s=input()
temp=0
for i in s:
    if s.count(i)%2==1:temp+=1
if temp%2==0 and temp!=0:
    print("Impossible")
else:
    step=0
    while len(s)>1:
        if s.count(s[0:1])==1:
            step += len(s) // 2
            s=s[len(s)//2:len(s)//2+1]+s[1:len(s)//2]+s[0:1]+s[len(s)//2+1:]
        else:
            step += len(s) - s.rfind(s[0:1]) - 1
            s=s[1:s.rfind(s[0:1])]+s[s.rfind(s[0:1])+1:]
    print(step)