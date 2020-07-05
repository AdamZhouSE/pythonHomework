s=input()
n=int(input())
count=0
for i in range(n):
    pwd=input()
    step=len(s)-8
    for j in range(0,step+1):
        if sorted(pwd)==sorted(s[j:j+8]):
            count+=1
print(count)