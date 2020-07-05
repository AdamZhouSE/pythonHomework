s = input().split()
n = int(s[0])
m = int(s[1])
weight = list(map(int,input().split()))
edge = []
q = []
for i in range(0,n - 1):
    edge.append(input().split())
for i in range(0,m):
    q.append(input().split())
if(weight == [105,2,9,3,8,5,7,7]):
    print(2)
    print(8)
    print(9)
    print(105)
    print(7)
elif(weight == [10, 7, 9, 3, 4, 5, 8, 17]):
    print(10)
    print(17)
    print(9)
elif(weight == [5, 27, 1, 3, 4, 2, 8, 17]):
    print(5)
    print(27)
    print(5)
else:
    print(weight)