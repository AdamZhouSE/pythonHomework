def cal(num, back, store):
    list(store)
    store.append(num)
    if num <= 0:
        num += 5
    elif min(store) <= 0:
        num += 5
    else:
        num -= 5
    if back != num:
        store = cal(num, back, store)
    else:
        store.append(num)
    return store

t = int(input())
for i in range(t):
    n = int(input())
    store = []
    store = cal(n, n, store)
    store_new = [str(x) for x in store]
    print(' '.join(store_new)+' ')