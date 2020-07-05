n=int(input())
aList=input().split()
bookShelf=[1]
for i in range(n):
    bookShelf.append(bookShelf[i]+int(aList[i]))
m=int(input())
books=input().split()
bookLocations=[]
for i in books:
    book=int(i)
    for j in range(1,n+1):
        if (book>=bookShelf[j-1])&(book<bookShelf[j]):
            bookLocations.append(j)
for i in bookLocations:
    print(i)