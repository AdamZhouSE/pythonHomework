nums = input().strip("[]").split(",")
nums = list(map(int,nums))
orders = []
for i in nums:
    loc = 0
    for j in orders:
        if i < j:
            break
        loc = loc + 1
    orders.insert(loc,i)
print(orders)