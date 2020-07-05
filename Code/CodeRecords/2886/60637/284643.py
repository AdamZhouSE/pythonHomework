sock_nums=(int)(input())
socks=input().split(' ')
max_num=0
desk=[]
for i in socks:
    if(i not in desk):
        desk.append(i)
    else:
        desk.remove(i)
    if(len(desk)>max_num):
        max_num=len(desk)
print(max_num)