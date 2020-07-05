def solution(lst:list):
    lst=sorted(lst,key=len)
    l1=len(lst[0])
    length=[i for i in range(l1,len(lst[-1])+1)]
    lr=[]
    tmp=[0]
    beg=0
    for i in range(len(lst)):
        if len(lst[i])>len(lst[beg]):
            tmp.append(i-1)
            lr.append(tmp)
            beg=i
            tmp=[beg]
    tmp.append(len(lst)-1)
    lr.append(tmp)
    for rag in lr:
        for x in range(rag[0],rag[1]):
            for y in range(x+1,rag[1]+1):
                if lst[x]==lst[y]:
                    return True
    for i in range(len(lr)-1):
        bef=lr[i]
        lat=lr[i+1]
        for j in range(bef[0],bef[1]+1):
            for k in range(lat[0],lat[1]+1):
                if lst[k][0:len(lst[j])]==lst[j]:
                    return True
    return False



if __name__=="__main__":
    teams=[]
    s=[]
    line=input()
    k=0
    while k<50:
        try:
            while line!='9':
                s.append(line)
                line=input()
            else:
                teams.append(s)
                s=[]
                line=input()
            k+=1
        except EOFError:
            break
    cnt=1
    for s in teams:
        res=solution(s)
        if res:
            print("Set {} is not immediately decodable".format(cnt))
        else:
            print("Set {} is immediately decodable".format(cnt))
        cnt+=1