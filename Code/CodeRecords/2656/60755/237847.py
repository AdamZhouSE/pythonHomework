def find(a, b):
    A = bin(int(a))[2:]
    B = bin(int(b))[2:]
    while len(A) != 10:
        A = "0" + A
    while len(B) != 10:
        B = "0" + B
    for i in range(1, 10):
        if A[-i] != B[-i]:
            return i



NumOfEg = int(input())
result = []
for i in range(NumOfEg):
    num = input().split(" ")
    result.append(find(num[0], num[1]))
for i in result:
    print(i)