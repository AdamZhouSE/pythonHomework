s=input()
l=s[1:len(s)-1].split(",")
l1=[]
for i in l:
    l1.append(int(i))
l1.sort()
print(l1)