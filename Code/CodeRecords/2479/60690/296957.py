n=int(input())
res = []
for j in range(n):
    s1=input()
    s2=input()
    this=[]
    for i in range(len(s1)):
        if s1[i] not in s2 and s1[i] not in this:
            this.append(s1[i])
    for i in range(len(s2)) :
        if s2[i] not in s1 and s2[i] not in this:
            this.append(s2[i])
    this.sort()
    s=""
    for i in range(len(this)):s+=this[i]    
    res.append(s)
for e in res:
    print(e,end="\n\n")