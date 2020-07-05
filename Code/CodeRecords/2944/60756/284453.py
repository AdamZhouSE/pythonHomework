s=list(input())
L=0
R=0
for i in s:
    if i=='(':
        L+=1
    elif i==')':
        R+=1
    if R>L:
        break
print("YES" if L==R else "NO", end="")