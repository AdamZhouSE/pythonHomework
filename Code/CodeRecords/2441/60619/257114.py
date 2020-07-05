numbers = eval(input())
after = []
for i in range(len(numbers)):
    after.append(-1)
head = 0
for i in range(1, len(numbers)):
    if numbers[i] < numbers[head]:
        after[i] = head
        head = i
    else:
        pre = 0
        position = head
        while position != -1 and numbers[i] > numbers[position]:
            pre = position
            position = after[position]
        after[pre] = i
        after[i] = position
result = []
while head != -1:
    result.append(numbers[head])
    head = after[head]
print(result)