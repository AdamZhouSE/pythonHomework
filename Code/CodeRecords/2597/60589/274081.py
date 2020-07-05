class flower(object):
    def __init__(self,w,c):
        self.w=w
        self.c=c


l=[]
action=input().strip()
while action!='-1':
    if action=='2' and len(l)>0:
        l.sort(key=lambda x: x.c)
        l.pop()
    elif action=='3' and len(l)>0:
        l.sort(key=lambda x: x.c)
        l.pop(0)
    else:
        action=action.split(' ')
        c=int(action[2])
        same=False
        for f in l:
            if c==f.c:
                same=True
                break
        if same:
            action=input().strip()
            continue
        l.append(flower(int(action[1]),int(action[2])))
    action=input().strip()
sum_w=0
sum_c=0
for f in l:
    sum_w+=f.w
    sum_c+=f.c
print(str(sum_w)+' '+str(sum_c),end='')