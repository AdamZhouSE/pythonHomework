src=eval(input())
ans=[]
def check(a1,a2):
    for a in a2:
        if a not in a1:
            return False
    return True
if src==sorted(src,reverse=True):
    print(1)
elif src==sorted(src):
    print(len(src))
else:
    start=0
    curr = 0
    l = 1
    std=[0]
    while curr<len(src):
        if check(src[start:curr+1],std):
            ans.append(src[start:curr+1])
            l=1
            start=curr+1
            std=[curr+1]
        else:
            std.append(curr+1)
            l+=1
        curr+=1
    print(len(ans))