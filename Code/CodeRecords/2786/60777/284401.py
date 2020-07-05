n=int(input())
get=input()
temp=[int(x) for x in get.split(' ')]
d=1
while(True):
    if(temp==[]):
        d-=1
        break
    pre=min(temp)
    temp.remove(pre)
    if(pre>=d):
        d+=1
        continue
    else:
        continue
        
print(d)
    