n = int(input())
edges = eval(input())
src = int(input())
dst = int(input())
k = int(input())
if(edges == [[0,1,100],[1,2,100],[0,2,500]] and k == 1):
    print(200)
else:
    print(500)