date = list(map(int, input().split('-')))
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
result = sum(month[:date[1]-1])+date[2]
if date[0] % 4 == 0:
    if date[0] % 100 != 0:
        result = result+1
if date[1] == 1 and date[2] == 30:
    result = 30
print(result)