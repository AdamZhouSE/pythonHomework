num=int(input())
for i in range(num):
    NQ=input()
    line=input()
    n=int(NQ.split(' ')[0])
    q=int(NQ.split(' ')[1])
    operate = line.split(' ')
    unread=[]
    read=[]
    trash=[]
    for j in range(n):
        unread.append(j+1)
    for k in range(2*q):
        if(k%2==0):
            target=int(operate[k+1])
            if(operate[k]=='1'):
                unread.remove(target)
                read.append(target)
            if(operate[k]=='2'):
                read.remove(target)
                trash.append(target)
            if(operate[k]=='3'):
                unread.remove(target)
                trash.append(target)
            if(operate[k]=='4'):
                trash.remove(target)
                read.append(target)
    if(len(unread)!=0):
        num_list_new = [str(x) for x in unread]
        print(' '.join(num_list_new)+' ')
    else:
        print('empty')
    if (len(read) != 0):
        num_list_new = [str(x) for x in read]
        print(' '.join(num_list_new)+' ')
    else:
        print('empty')
    if (len(trash) != 0):
        num_list_new = [str(x) for x in trash]
        print(' '.join(num_list_new)+' ')
    else:
        print('empty')