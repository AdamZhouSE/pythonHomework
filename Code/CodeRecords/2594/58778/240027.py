n=int(input())
for i in range(n):
    s=input()
    cl=[]
    for x in range(len(s)):
        if(s.count(s[x:x+1])!=1):
            cl.append(s[x:x+1])
    ml=[]
    if(len(cl)==0):
        print(-1)
        break
    for x in cl:
        ml.append(s.rfind(x)-s.find(x)-1)
    print(max(ml))