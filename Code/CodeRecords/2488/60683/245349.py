src = eval(input())
src.sort()
for i in range(2, len(src),2):
    temp = src[i]
    src[i] = src[i - 1]
    src[i - 1] = temp
print(src)