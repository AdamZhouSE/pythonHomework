nums = input().split(' ')
total = int(nums[0])
time = int(nums[1])
books = input().split(' ')
for i in range(0,total):
    books[i] = int(books[i])
books.sort()
sum = 0
i = 0
while time>=0:
    sum+=1
    time-=books[i]
    i+=1
sum-=1
print(sum)