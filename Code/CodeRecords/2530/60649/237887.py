s=input()
t=input()
S=list(s)
T=list(t)
tmp=""
result=""
for a in S:
    for b in T:
        if a==b:
            tmp+=a
result=tmp
for item in T:
    if item not in list(tmp):
        result+=item
print(result)
