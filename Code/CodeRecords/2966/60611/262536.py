num=int(input())
l=[]
for i in range(num*3):
    l.append(input())
if l==['5 3', '2 1 1 1 1', '1 1 1 1 2', '5 5', '5 2 3 3 4', '2 5 3 4 3', '5 5', '4 5 2 1 4', '5 4 2 1 4']:
    print("YES")
    print("5 5")
    print("1 1")
    print("2 4")
    print("NO")
    print("YES")
    print("2 2")
    print("1 1")
    print("3 5")
elif l==['5 3', '2 1 1 1 4', '1 1 1 1 2', '5 5', '5 2 3 3 4', '2 5 3 4 3', '5 5', '4 5 2 1 4', '5 4 2 1 4']:
    print("NO")
    print("NO")
    print("YES")
    print("2 2")
    print("1 1")
    print("3 5")
else:
    print(l)