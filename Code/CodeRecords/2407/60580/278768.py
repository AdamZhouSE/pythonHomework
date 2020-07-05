s = input()
l = s.split('-')
year = int(l[0])
month = int(l[1])
day = int(l[2])
lyear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
count = 0
if year % 4 ==0:
    lyear[1] = 29
for i in range(0, month-1):
    count += lyear[i]
count += day
print(count)