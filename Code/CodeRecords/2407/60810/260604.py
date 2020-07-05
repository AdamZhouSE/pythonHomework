date = input()
year, month, day = map(int, date.split("-"))
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    months[2] +=1

res = 0
for i in range(month):
    res += months[i]
res += day
print(res)