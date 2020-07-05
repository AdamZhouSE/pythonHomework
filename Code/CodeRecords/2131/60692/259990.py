A = input().split(",")
A = [int(i) for i in A]
count = 0


def counter(list1: list):
    measure = list1[1] - list1[0]
    for i in range(1, len(list1) - 1):
        if list1[i + 1] - list1[i] != measure:
            return 0
    return 1


for i in range(len(A) - 2):
    for j in range(i + 2, len(A)):
        count += counter(A[i:j + 1])
print(count)