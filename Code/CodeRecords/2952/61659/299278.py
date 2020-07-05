order=input()
printList=[]
nowWord=""
for x in order:
    if x=='B':
        nowWord=nowWord[0:len(nowWord)-1]
    else:
        if x=="P":
            printList.append(nowWord)
        else:
            nowWord=nowWord+x

x=int(input())
for k in range(0,x):
    temp=list(input().split(" "))
    print(printList[int(temp[1])-1].count(printList[int(temp[0])-1]))
