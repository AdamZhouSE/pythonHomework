A = input().split(",")
A = list(map(int,A))
B = input().split(",")
B = list(map(int,B))
C = input().split(",")
C = list(map(int,C))
D = input().split(",")
D = list(map(int,D))
count = 0
for i in A:
    for j in B:
        for k in C:
            for l in D:
                if i + j + k + l == 0:
                    count = count + 1
print(count)