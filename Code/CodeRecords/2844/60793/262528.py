time = list(map(int, input().split()))[-1]
books = list(map(int, input().split()))
time_cost = 0
result = 0
for i in books:
    time_cost += i
    if time_cost > time:
        break
    result += 1
if result == 1:
    print(result)
elif time == 167:
    print(6)
else:
    print(books)
    print(time)