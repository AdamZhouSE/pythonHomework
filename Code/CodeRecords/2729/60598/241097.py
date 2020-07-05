nums = list(map(int, input()[1:-1].split(",")))
store = set()
for i in nums:
    if not i in store:
        store.add(i)
    else:
        store.remove(i)
print(store.pop())
