n = int(input())
string = input().split()
nums = []
odd = []
even = []
for x in string:
    nums.append(int(x))
    if int(x) % 2 == 0:
        even.append(int(x))
    else:
        odd.append(int(x))
result = 0
odd.sort()
even.sort()
if len(odd) > len(even):
    for x in range(len(odd) - len(even) - 1):
        result += odd[x]
elif len(odd) < len(even):
    for x in range(len(even) - len(odd) - 1):
        result += even[x]
print(result)
