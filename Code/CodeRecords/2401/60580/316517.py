num = int(input())
count = 0
ans = [num]
while 2 ** count < num:
    count = count + 1
if count % 2 == 0:
    num = 2 ** count - (num - 2 ** (count - 1)) - 1
for i in range(count - 1, 0, -1):
    num = int(num / 2)
    if i % 2 == 1:
        ans.append(num)
    else:
        ans.append(2 ** i - (num - 2 ** (i - 1)) - 1)
ans = ans[::-1]
print(ans)
