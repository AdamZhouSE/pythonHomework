t = int(input())
for i in range(t):
    n = int(input())
    inp = [int(x) for x in input().split(" ")]
    K = int(input())
    multiply = 1
    for num in inp:
        multiply *= num
    print(multiply % K)
