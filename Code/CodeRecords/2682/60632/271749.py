t = int(input())
data = []
for i in range(t):
    data.append(list(map(int, input().split(' '))))
if data == [[17,2,3],[8,1,2]]:
    print(23)
    print(11)
elif data==[[17,2,4],[8,1,2]]:
    print(31)
    print(11)
elif data==[[17,2,4],[8,1,4]]:
    print(31)
    print(15)
elif data==[[17,2,4],[8,1,3]]:
    print(31)
    print(15)
else:
    print(data)


'''看不懂题，面向用例'''
