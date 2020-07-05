n = eval(input())
size = eval(input())
temp = []
while(n != 0):
    n -= 1
    temp.append(eval(input()))

temp.sort(reverse=True)
count = 0
for num in temp:
    if(num > size):
        if(size==0):
            break
        count += 1
        break
    else:
        size -= num
        count += 1
print(count)