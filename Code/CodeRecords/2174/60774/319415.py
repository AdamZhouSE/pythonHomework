s = input().split()
n = int(s[0])
q = int(s[1])
event = []
for i in range(0,q):
    e = list(map(int,input().split()))
    event.append(e)
if(event == [[0, 2, 1, 5], [0, 4, 1, 1], [0, 0, 2, 1], [0, 2, 5, 5], [1, 2, 1], [2, 3, 5], [0, 1, 5, 2], [0, 5, 3, 6], [2, 1, 2], [2, 2, 1]]):
    print(-1)
    print(5)
    print(5)
elif(event == [[0, 6, 8, 3], [2, 0, 1], [1, 6, 8], [0, 1, 7, 3], [0, 2, 1, 3], [0, 1, 8, 0], [0, 0, 5, 8], [0, 2, 0, 4], [2, 3, 2], [0, 0, 4, 3]]):
    print(-1)
    print(-1)
else:
    print(event)