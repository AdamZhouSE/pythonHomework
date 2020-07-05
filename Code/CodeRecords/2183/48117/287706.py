questNum = int(input())

for quest in range(questNum):
    line = int(input())
    
    end = 0
    for l in range(1, line + 1):
        end += l * 2
    
    sum = 0
    for i in range(1, end + 1):
        sum += i
    
    print(sum)