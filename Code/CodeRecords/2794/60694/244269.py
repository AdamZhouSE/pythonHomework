n = int(input())
bookL = list(map(int, input().split()))
m = int(input())
pageNoL = list(map(int, input().split()))

intervals = [ [1, bookL[0]] ]
for i in range(1, n):
    intervals.append([sum(bookL[:i])+1, sum(bookL[:i])+bookL[i]])
for i in range(m):
    for j in range(n):
        if intervals[j][0] <= pageNoL[i] <= intervals[j][1]:
            print(j+1)
