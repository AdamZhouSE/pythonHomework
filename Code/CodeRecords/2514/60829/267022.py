s=str(input())
t=str(input())
for i in range(0,len(s)):
    k=0
    judge=0
    for j in range(k,len(t)):
        if s[i]==t[j]:
            k=j
            break
    if j==len(t)-1 and not k==len(t)-1:
        judge=1
        print("False")
        break
if judge==0:
    print("True")