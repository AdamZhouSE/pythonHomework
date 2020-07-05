def dictionary():
    N=int(input())
    paper=[]
    query_li=[]
    dic={}
    for i in range(0,N):
        paper.append(input().split(" "))
    M=int(input())
    for i in range(0,M):
        query_li.append(input())
    for item in paper:
        L=int(item[0])
        for i in range(1,L+1):
            if item[i] not in dic.keys():
                dic[item[i]]=[paper.index(item)+1]
            else:
                dic[item[i]].append(paper.index(item)+1)
    for query in query_li:
        if query not in dic.keys():
            print(" ")
        else:
            for idx in dic[query]:
                print(idx,end=" ")
            print()

if __name__=='__main__':
    dictionary()
