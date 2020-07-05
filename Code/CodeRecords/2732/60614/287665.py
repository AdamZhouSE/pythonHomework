questions=int(input())
for i in range(questions):
    init=[int(x) for x in input().spkit()]
    print(pow(init[0],init[1])%init[2])