num=int(input())
for k in range(num):
    l1=input().split(" ")
    n1=int(l1[0])
    n2=int(l1[1])
    board1=[]
    for i in range(n1):
        l=input().split(" ")
        for j in range(len(l)):
            l[j]=int(l[j])
        board1.append(l)
    board2 = []
    for i in range(n1):
        l = input().split(" ")
        for j in range(len(l)):
            l[j] = int(l[j])
        board2.append(l)
    #print(board1)
    #print(board2)
    '''for i in range(n1):
        for j in range(n1):
            board1[i][j]=board1[i][j]+board2[i][j]
    sum=0
    for i in range(n1):
        for j in range(n1):
            if board1[i][j]==n2:
                sum=sum+1'''
    sum=0
    for i in range(n1):
        for j in range(n1):
            n=n2-board1[i][j]
            for m in range(len(board2)):
                if n in board2[m]:
                    sum=sum+1
    print(sum)