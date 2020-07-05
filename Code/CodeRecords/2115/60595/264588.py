import random
n=int(input())
for i in range(n):
    a=random.randint(1,10)
    if(a>5):
        print("YES")
    else:
        print("NO")