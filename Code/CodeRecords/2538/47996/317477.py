nums = [int(x) for x in input()[1:-1].split(",")]
number = 1
while True:
    if number not in nums:
        break
    else:
        number += 1
print(number)
