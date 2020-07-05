nandm=input().split(" ")
n=int(nandm[0])
m=int(nandm[1])
candidate=[]
for _ in range(n):
    candidate.append(0)
for _ in range(m):
    ans=list(map(int,input().split(" ")))
    for t in range(n):
        candidate[t]+=ans[t]
candidate=sorted(candidate)
maxvalue=candidate[-1]
def search(candidate,maxvalue):
    for h in range(len(candidate)):
        if candidate[h]==maxvalue:
            return h
print(search(candidate,maxvalue))