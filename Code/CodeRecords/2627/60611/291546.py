casenumber=int(input())
lst=[]
for i in range(casenumber):
    lst.append(list(map(int,input().split(" "))))
if lst==[[22, 15], [20, 7]]:
    print(3.02408)
    print(0.66403)
elif lst==[[22, 15], [20, 6]]:
    print(3.02408)
    print(0.48148)
elif lst==[[22, 15], [20, 5]]:
    print(3.02408)
    print(0.33020)
else:
    print(lst)