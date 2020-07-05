s1=input()
s2=input()
n1=len(s1)
count=0
wide=0
while wide<n1:
    for i in range(0,n1-wide):
        s=s1[i:i+wide+1]
        count+=s2.count(s)
    wide+=1
print(count)    