import sys

lst = []
for line in sys.stdin:
    if line.strip() == '':
        break
    lst.append(line)

bucket = int(lst[0])
minutesToDie = int(lst[1])
minutesToTest = int(lst[2])

testTimes = int(minutesToTest/minutesToDie)

pigNumber = 1

while True:
    if pow(pigNumber+1,testTimes)>bucket:
        break
    pigNumber += 1

print(pigNumber)