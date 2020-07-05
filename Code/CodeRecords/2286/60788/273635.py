line1=input().strip()
length=int(line1.split()[0])
s=[1]*(length+1)
num=int(line1.split()[1])
for i in range(num):
    line=input().strip()
    start=int(line.split()[0])
    end=int(line.split()[1])
    for i in range(start,end+1):
        s[i]=0
print(s.count(1))