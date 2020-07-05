temp=input().split('"')
letter=[]

for i in temp:
    if('a'<=i and i<='z'):
        letter.append(i)
        
tar=input()
res=max(letter)

if(max(letter)<=tar):
    res=min(letter)
else:
    for i in temp:
        if(i>tar and i<res):
            res=i

print(res)