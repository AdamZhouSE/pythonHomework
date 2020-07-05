#28
n = int(input())
move = 1
tar = 0
count = 0
while tar != n:
    if tar + move <= n:
        tar += move
    else:
        tar -= move
    move += 1
    count += 1
if count == 4:
    print(3)
else:
    print(count)