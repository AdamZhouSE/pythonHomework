def switch(num):
    return 0 if num == 1 else 1

num = int(input())
light = [ 0 for i in range(num+1)] #0代表关闭，1代表开启,light[0]仅仅是占位，无意义
for i in range(1,num+1):
    j = i
    while j <= num:
        light[j] = switch(light[j])
        j = j + i

count = 0
for e in light:
    if e == 1:
        count += 1

print(count)