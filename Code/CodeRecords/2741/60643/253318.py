lst=input()
i=0
j=i+1
cnt=1
stor=[]
while j<len(lst):#j到lst最后一个字符
    if lst[j]<=lst[i]:
        i=j
        j=i+1
        stor.append(cnt)
        cnt=1
    else:
        j+=1
        i+=1
        cnt+=1
print(max(stor))
