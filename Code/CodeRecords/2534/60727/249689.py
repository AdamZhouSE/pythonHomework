li=input()
d=[]
for i in range(0,len(li)):
    if li[i].isdigit():
        d.append(int(li[i]))
print(sorted(d))