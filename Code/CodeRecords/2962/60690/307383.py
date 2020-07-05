s=input().split(" ")
n=int(s[0])
length=int(s[1])
ss=input().split(" ")
res=[]
hash_=[]
for i in range(length):
    hash_.append(-1)
for i in range(len(ss)):
    this=(ord(ss[i][-3])-ord('A'))*(32**2)+(ord(ss[i][-2])-ord('A'))*32+(ord(ss[i][-1])-ord('A'))
    index=this%length
    if hash_[index]==-1:
        hash_[index]=1
        res.append(index)
    else:
        di=1
        while True:
            if hash_[(index+di**2+length)%length]==-1:
                hash_[(index+ di ** 2 + length) % length] =1
                res.append((index+di**2+length)%length)
                break
            elif hash_[(index-di**2+length)%length]==-1:
                hash_[(index - di ** 2 + length) % length] =1
                res.append((index - di ** 2 + length) % length)
                break
            else:
                di+=1
for i in range(len(res)-1):print(res[i],end=" ")
print(res[-1])

