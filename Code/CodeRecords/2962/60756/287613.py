def conflict(x:int,hashTable:list)->int:
    i=1
    P=len(hashTable)
    while hashTable[x]:
       for temp in ((x+i*i)%P,(x-i*i)%P):
           if not hashTable[temp]:
               return temp
       i+=1

def c2I(x:str)->int:
    return ord(x)-ord('A')
N,P=map(int,input().split())
arr=list(map(list,input().split()))
hashTable=[0 for i in range(P)]
ans=[]
for i in range(N):
    x=(c2I(arr[i][-3])*32**2+c2I(arr[i][-2])*32+c2I(arr[i][-1]))%P
    if hashTable[x]:
        x=conflict(x,hashTable)
    hashTable[x]=1
    ans.append(str(x))
print(' '.join(ans))