n=int(input())
temp=[int(x) for x in input().split(' ')]
test=temp.copy()
def square(x):
    for i in range(0,x+1):
        if(i**2==x):
            return True
    return False

find=False
res=0
while(not find):
    pre=max(temp)
    if(not square(pre)):
        find=True
        res=pre
    temp.remove(pre)
print(res)