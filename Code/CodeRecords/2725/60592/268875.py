import random
tests = int(input())
for i in range(0,tests):
    i = random.uniform(0,100)
    if i > 35:
        print(1)
    else:
        print(0)