n = int(input())
for i in range(0,n):
    a = input()
    diff =[]
    A = input().split(" ")
    B = input().split(" ")
    for j in range(0,len(A)):
        if A[j] in B:
            diff.append(A[j])

    print(len(list(set(diff))))