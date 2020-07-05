def like(a,b):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            x=a[i]
            y=a[j]
            temp=a[0:i]+y+a[i+1:j]+x+a[j+1:]
            if temp==b:
                return True
    return False

get=eval(input())
temp=[[0]]

for i in range(len(get)):
    for j in range(i+1,len(get)):
        if(like(get[i],get[j])):
            zai=False
            for k in range(len(temp)):
                if i in temp[k] or j in temp[k]:
                    temp[k].append(i)
                    temp[k].append(j)
                    zai=True
                    break
            if(not zai):
                temp.append([i,j])
for i in range(len(get)):
    for j in temp:
        if(i in j):
            break
        if(j==temp[-1]):
            temp.append([i])
print(len(temp))