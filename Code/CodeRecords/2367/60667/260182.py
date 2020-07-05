one = [1,11,111,1111,11111,111111,1111111,11111111,111111111,1111111111]
k = int(input())
for i in one:
    if i >= k and i % k == 0:
        print(one.index(i)+1)
        quit()
print(-1)        