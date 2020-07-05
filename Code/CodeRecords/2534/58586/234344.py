lines=input()
res=[]
for i in range(len(lines)):
    if lines[i].isalnum():
        res.append(int(lines[i]))
res.sort()
print(res)