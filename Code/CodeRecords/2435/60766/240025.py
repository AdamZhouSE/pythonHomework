def findmaxOrder(dic):
    print(max(dic))

if __name__ == '__main__':
    line=input().split()
    n=int(line[0])
    m=int(line[1])
    dic=[]#n
    que=[]#m
    
    for i in range(n):
        dic.append(input())
    for i in range(m):
        line=input().split()
        que.append(list(map(int, line)))
        
    #print(dic)
    #print(que)
    
    for i in range(m):
        findmaxOrder(dic[que[i][0]-1:que[i][1]])