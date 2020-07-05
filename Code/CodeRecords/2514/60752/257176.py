s1=input()
s2=input()
end=-1
start=0
count=0
rs=False
while start<len(s2) and count<len(s1):
    if s2[start:].find(s1[count])>end:
        end=s2[start:].find(s1[count])
        count+=1
        if count==len(s1):
            rs=True
            break
    if s2[start:].find(s1[count])==-1:break
    start+=1
print(rs)