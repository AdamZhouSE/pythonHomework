row = int(input())
second = row%26
first = row//26
result = ""
if first==0:
    result = chr(ord('A')+second-1)
else:
    result = chr(ord('A')+first-1)
    result = result+chr(ord('A')+second-1)
print(result)