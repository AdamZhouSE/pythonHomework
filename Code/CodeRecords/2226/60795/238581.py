left=int(input())
right=int(input())
list=[]
for i in range(left,right):
    th=i%10000
    th=th/1000
    hu=th%1000
    hu=th/100
    de=hu%10
    if th>0&hu>0&de>0:
        if i%th==0&i%hu==0&i%de==0:
            list.append(i)
    elif hu>0&de>0:
        if i%hu==0&i%de==0:
            list.append(i)
    elif de>0:
        if i%de==0:
            list.append(i)
print(list)

