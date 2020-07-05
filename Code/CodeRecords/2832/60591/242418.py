input()
book = list(map(int,input().split(" ")))
num = 0
now = 1
for x in range(len(book)):
    if(now == book[x]):
        num += 1
        now += 1
        continue
    if(book[x] > now):
        now = book[x]
print(num)