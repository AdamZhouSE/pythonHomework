def find(string):
    count = 0
    for m in string:
        if(m in "47"):
            count += 1
    return count

k = int(input().split(" ")[1])
nums = input().split(" ")

count = 0
for num in nums:
    if(find(num) <= k):
        count += 1
print(count)