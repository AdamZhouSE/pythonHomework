A = input().split(",")
B = [int(x) for x in A]
B.sort()
target = int(input())
print(B[len(B)-target])
