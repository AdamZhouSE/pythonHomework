a=int(input())
b=input().split(" ")
print(b)
store=[]
for i in range(0,2*a):
    store.append(list(map(int, input().split(" "))))
print(store[0])
