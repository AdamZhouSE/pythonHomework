# 4
inp = input()
n,x = inp.split()
n = int(n)
x = int(x)

inp = input()
chapter_num = inp.split()

for i in range(len(chapter_num)):
    chapter_num[i] = int(chapter_num[i])
chapter_num.sort()

time_sum = 0
for i in range(n):
    if x == 1:
        time_sum = time_sum + chapter_num[i]
    else:
        time_sum = time_sum + x*chapter_num[i]
        x = x -1

print(time_sum)