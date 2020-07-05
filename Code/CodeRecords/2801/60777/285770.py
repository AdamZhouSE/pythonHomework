n=int(input())
temp=[int(x) for x in input().split(' ')]
find=False
while(len(temp)>=3):
    f=min(temp)
    temp.remove(f)
    s=min(temp)
    temp.remove(s)
    for i in range(len(temp)):
        if(f+s>temp[i]):
            find=True
    temp.append(s)
if(find):
    print("YES")
else:
    print("NO")