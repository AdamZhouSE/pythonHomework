numList=input().split()
string=input().split()
hint=input().split()
ans=[]
for x in string:
    if x in hint:
        ans.append(x)
print(str(" ".join(ans)))