t=int(input())
for k in range(0,t):
    n=int(input())
    proj=input().split(' ')
    ids={} #ids is a dictionary
    for i in range(0,n):
        if proj[i] in ids:
            ids[proj[i]]=ids[proj[i]]+1
        else:
            ids[proj[i]]=1
    ids_v=sorted(ids.values())#取出字典的value并排序
    m=int(input())
    nums=len(ids_v)
    for j in ids_v:
        if m-j<0:
            break       
        else :
            m=m-j
            nums=nums-1
    print(nums)
    ids.clear()
    