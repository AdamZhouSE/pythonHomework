a=int(input())
print(a)
store=[]
for i in range(0,2*a):
    store.append(list(map(int, input().split(" "))))
print(store[0])
