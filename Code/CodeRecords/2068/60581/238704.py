import sys

lst = []
for line in sys.stdin:
    if line.strip() == '':
        break
    lst.append(line)

dividend = int(lst[0])
divisor = int(lst[1])

signal = True
if dividend < 0:
    dividend = -dividend
    signal = not signal
if divisor < 0:
    divisor = -divisor
    signal = not signal

count = 0
while dividend > 0:
    dividend -= divisor
    count += 1

count -= 1
if not signal:
    count = -count

print(count)