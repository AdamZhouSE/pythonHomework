ins=input()
temp=ins
m=int(input())
rec=[];i=0
while i <len(ins):
    if ins[i]=='P':
        rec.append(ins[:i])
        ins=ins[:i]+ins[i+1:]
        i-=1
    elif ins[i]=='B':
        ins=ins[:i-1]+ins[i+1:]
        i-=2
    i+=1
for _ in range(m):
    s=input().split(' ');s=[int(x) for x in s]
    if s[0]<=len(rec) and s[1]<=len(rec):
        print(rec[s[1]-1].count(rec[s[0]-1]))
    else:
        print(0)