s1=input().split(" ")
nA=int(s1[0])
nB=int(s1[1])
s2=input().split(" ")
k=int(s2[0])
m=int(s2[1])
s3=input().split(" ")
s4=input().split(" ")
for i in range(nA):
    s3[i]=int(s3[i])
for j in range(nB):
    s4[j]=int(s4[j])
s3.sort()
s4.sort()
if s3[k-1]<s4[len(s4)-k]:
    print("YES")
else:
    print("NO")