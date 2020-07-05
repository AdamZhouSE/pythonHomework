time_limit = list(map(int, input().split()))[-1]
books = list(map(int, input().split()))
time_cost = 0
max_books = 0
result = 0
for i in range(0, len(books)):
    for j in range(i, len(books)):
        time_cost += books[j]
        if time_cost > time_limit:
            break
        max_books += 1
    time_cost = 0
    if max_books > result:
        result = max_books
        max_books = 0
print(result)