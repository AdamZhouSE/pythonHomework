num=int(input())
list=[int(n) for n in input().split(' ')]
lch,rch=[],[]
print(-1)
root=list[0]
tree=[]
for i in range(0,len(list)):
    tem=[list[i],0,0]
    tree.append(tem)
for i in range(1,len(list)):
    if list[i]<root:
        if len(lch)==0:
           lch.append(list[i])
           tree[0][1]=1
           print(root)
        else:
            pos = -1
            for j in range(0, len(lch)):
                if list[i] < lch[j]:
                    pos = j
                    break

            if pos == -1:
                lch.append(list[i])
                le = len(lch)
                print(lch[le - 2])
                index = list.index(lch[le - 2])
                tree[index][2] = 1
            else:
                index = list.index(lch[pos])
                if tree[index][1] == 0:
                    print(lch[pos])
                    lch.insert(pos, list[i])
                    tree[index][1] = 1
                else:
                    ino = list.index(lch[pos - 1])
                    if tree[ino][2] == 0:
                        print(lch[pos - 1])
                        lch.insert(pos, list[i])
                        tree[ino][2] = 1
    if list[i]>root:
        if len(rch)==0:
           rch.append(list[i])
           tree[0][2]=1
           print(root)
        else:
            pos=-1
            for j in range(0,len(rch)):
                if list[i]<rch[j]:
                    pos=j
                    break

            if pos==-1:
                rch.append(list[i])
                le=len(rch)
                print(rch[le-2])
                index=list.index(rch[le-2])
                tree[index][2]=1
            else:
                index = list.index(rch[pos])
                if tree[index][1]==0:
                   print(rch[pos])
                   rch.insert(pos,list[i])
                   tree[index][1]=1
                else:
                   ino=list.index(rch[pos-1])
                   if tree[ino][2]==0:
                       print(rch[pos-1])
                       rch.insert(pos,list[i])
                       tree[ino][2]=1

