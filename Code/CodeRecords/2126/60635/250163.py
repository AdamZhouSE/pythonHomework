src=[int(x) for x in input().split(',')]
ans=src[:]
index=0
while index < len(ans)-1:
    i = index +1
    while i<len(ans):
        if ans[i]%ans[index]==0:
            i +=1
        else:
            del ans[i]
    index += 1
print(ans)