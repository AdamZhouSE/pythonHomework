n=eval(input())
start=eval(input())
res = [i ^ (i // 2) for i in range(2 ** n)]
ans=[]
for i in range(len(res)):
    if res[i] == start:
        ans=res[i:] + res[:i]
print("[",end="")
for i in range(len(ans)):
    if i != len(ans)-1:
        print(ans[i],end=", ")
    else:
        print(ans[i],end="")
print("]")