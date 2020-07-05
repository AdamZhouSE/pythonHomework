s=input().split(" ")
n=int(s[0])
m=int(s[1])
lanterns=[]
for i in range(n):
    s=input().split(" ")
    for j in range(1,len(s)):
        if s[j] not in lanterns:
            lanterns.append(s[j])
if len(lanterns)==m:
    print("YES")
else:
    print("NO")