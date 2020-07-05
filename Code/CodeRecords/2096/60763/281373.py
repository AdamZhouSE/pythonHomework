x = int(input())
sqrt = 0
while sqrt*sqrt <= x:
    if sqrt*sqrt == x or (sqrt+1)*(sqrt+1) > x:
        break
    sqrt+=1
print(sqrt)