x = int(input())
result = ''
while x > 0:
    next = chr(ord('A')+((x-1) % 26))
    result = next + result
    x = int((x-1)/26)
print(result)