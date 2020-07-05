num=input()
s=0
m=1
for i in range(0,len(num)):
    m=m*int(num[i:i+1])
    s=s+int(num[i:i+1])
print(m-s)