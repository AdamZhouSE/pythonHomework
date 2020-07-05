dividened = int(input())
divisor = int(input())
reverse = False
if divisor < 0 and dividened > 0:
    reverse = True
    divisor = - divisor
answer = dividened // divisor
if reverse:
    answer = - answer

print(answer)