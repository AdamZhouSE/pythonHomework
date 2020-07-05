nums = input().split(' ')
total = int(nums[0])
time = int(nums[1])
books = input().split(' ')
for i in range(0,total):
    books[i] = int(books[i])
max = 0
mark = time
for j in range(0,total):
    sum = 0
    i = j
    time = mark
    while time>=0 and i < total:
        time-=books[i]
        sum+=1
        i+=1
    if max < sum:
        max = sum
print(max)