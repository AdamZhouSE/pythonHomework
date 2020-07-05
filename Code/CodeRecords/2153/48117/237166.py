num = list(input())

if num[0] == '-':
    answer = "-"
    end = 0
else:
    answer = ""
    end = -1



for index in range(len(num) - 1, end, -1):
    if index == len(num) - 1:
        if num[index] == "0":
            continue
    answer += num[index]

print(answer)
