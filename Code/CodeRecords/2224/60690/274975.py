s=input()
list=[]
res=""
l=len(s)
for e in s:list.append(int(e))
for i in range(l):
    if max(list)!=int(s[0]):
        index=0
        for i in range(len(list)-1,0,-1):
            if list[i]==max(list): index=i
        temp=max(list)
        list[index]=list[0]
        list[0]=temp
        for e in list: res+=str(e)
        break
    else:
        res+=s[0]
        s=s[1:]
        list.remove(max(list))

print(res)