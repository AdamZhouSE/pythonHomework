def factorial(n : int):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return factorial(n - 1) + factorial(n - 2)





questNum = int(input())

for quest in range(questNum):
    n = int(input())
    print(factorial(n))