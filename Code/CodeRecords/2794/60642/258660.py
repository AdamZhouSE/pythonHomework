input()
a = input().split()
bookCases = []
for i in range(len(a)):
    bookCases.append(int(a[i]))
input()
a = input().split()
books = []
for i in range(len(a)):
    books.append(int(a[i]))

for i in range(len(books)):
    for j in range(len(bookCases)):
        books[i] = books[i]-bookCases[j]
        if(books[i]<=0):
            print(j+1)
            break