n = eval(input())
stone = list(input())
result = [stone[0]]
for i in range(1,len(stone)):
    if stone[i] == result[-1]:
        continue
    else:result.append(stone[i])
print(len(stone)-len(result))
    
