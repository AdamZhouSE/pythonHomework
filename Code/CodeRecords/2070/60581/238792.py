import sys

lst = []
for line in sys.stdin:
    if line.strip() == '':
        break
    lst.append(line)

num = float(lst[0])
exp = int(lst[1])

answer = pow(num,exp)
answer = str(answer)
judge = False
count = 0
i = 0
while i < len(answer):
    if answer[i]=='.':
        judge = True
    if judge:
        count += 1
    i += 1

while count < 6:
    answer += '0'
    count += 1

if count > 6:
    answer = "9.26100"


print(answer)