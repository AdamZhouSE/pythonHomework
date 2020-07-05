num = list(input())

if num[0] == '-':
    answer = "-"
    end = 0
else:
    answer = ""
    end = -1

zeroIndex = 1
while zeroIndex < len(num):
    if num[zeroIndex] == "0":
        end += 1
    else:
        break
    
for index in range(len(num) - 1, end, -1):
    answer += num[index]

print(answer)
