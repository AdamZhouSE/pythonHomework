count = int(input())
ans = []
for i in range(0, count):
    para = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    A.extend(B)
    A.sort()
    ans.append(A[para[2]-1])
for i in ans:
    print(i)
