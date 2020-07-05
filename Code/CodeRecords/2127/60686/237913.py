num = int(input())
list_input = input().split(",")
num2 = 0
for i in range(len(list_input)):
    num2 *= 10
    num2 += int(list_input[i])
print(pow(num, num2) % 1337)
