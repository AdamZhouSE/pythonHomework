n = int(input())
ping1 = 'LIVE'
ping2 = 'LIVE'
num1 = 0
num2 = 0
for i in range(n):
    list = []
    list = input().split()
    if list[0] == '1':
        num1 = num1 + int(list[1]) - int(list[2])
    else:
        num2 = num2 + int(list[1]) - int(list[2])
if num1 < 0:
    ping1 = 'DEAD'
if num2 < 0:
    ping2 = 'DEAD'
print(ping1)
print(ping2)