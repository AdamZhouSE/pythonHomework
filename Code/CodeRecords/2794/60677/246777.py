floorNum=int(input())
floors=input().split()
floors=[int(x) for x in floors]
bookNum=int(input())
books=input().split()
books=[int(x) for x in books]

for i in range(bookNum):
    for j in range(floorNum):
        books[i]-=floors[j]
        if books[i]<=0:
            print(j+1)
            break