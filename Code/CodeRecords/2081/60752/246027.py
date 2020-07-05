s1=input()
s2=input()
size1=len(s1)
size2=len(s2)
count=0
for i in range(size1-size2+1):
    if s1[i:i+size2]==s2:count+=1
print(count,end='')



