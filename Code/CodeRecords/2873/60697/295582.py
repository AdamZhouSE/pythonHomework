size=list(map(int,input().split(' ')))
se=list(map(int,input().split(' ')))
button=list(map(int,input().split(' ')))
a=size[0]
b=size[1]
ans=[]
for i in range(a):
    if(se[i] in button):
        ans.append(str(se[i]))
print(" ".join(ans))
# 7 3
# 3 5 7 1 6 2 8
# 1 2 7

# 4 4
# 3 4 1 0
# 0 1 7 9