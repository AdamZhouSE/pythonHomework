n=int(input())
good=False
k=2

def same(s):
    tem='1'
    for x in s:
        if(x!=tem):
            return False
    return True

while(not good):
    temp=n
    strs=''
    while(temp>0):
        strs+=str(temp%k)
        temp=int(temp/k)
    strs=strs[::-1]
    if(same(strs)):
        break
    k+=1
    
print(k)
        
        