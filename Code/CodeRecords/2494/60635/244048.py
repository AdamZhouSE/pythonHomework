src = input()
array = [int(x) for x in src[1:len(src)-1].split(',')]
ans = 0
num = len(array)
for i in range(num-1):
    for j in range(i+1,num):
        if array[i]>2*array[j]:
            ans += 1
print(ans)
    