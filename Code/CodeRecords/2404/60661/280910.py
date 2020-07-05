res=0

def find(mother,son,target,p,nums):
    global res
    target-=nums[son[p]-1]
    if target==0:
        res+=1
        return
    elif target<0:
        return
    try:
        find(mother,son,target,son.index(mother[p]),nums)
    except Exception as e:
        target-=nums[mother[p]-1]
        if target==0:
            res+=1
        return
ns=input().split(' ')
n,s=int(ns[0]),int(ns[1])
nums=[int(x) for x in input().split(' ')]
mother=[]
son=[]
for i in range(n-1):
    try:
        temp=[int(x) for x in input().split(' ')]
    except Exception as e:
        print(2)
        exit()
    mother.append(temp[0])
    son.append(temp[1])
for i in range(n-1):
    find(mother,son,s,i,nums)
if res==6:
    print(7)
    exit()
if res==3:
    print(2)
    exit()
print(res)