def compare(num1,num2):
    if len(num1) > len(num2):
        length = len(num1)
        for i in range(length-len(num2)):
            num2 = num2 + num2[len(num2)-1]
    else:
        length = len(num2)
        for i in range(length-len(num1)):
            num1 = num1 + num1[len(num1)-1]
    for i in range(length):
        if num1[i]>num2[i]:
            return True
        elif num1[i]<num2[i]:
            return False
    return True
    

nums = input().strip("[]").split(",")
orders = []
for i in nums:
    loc = 0
    for j in orders:
        if compare(i,j):
            break
        loc = loc + 1
    orders.insert(loc,i)
output = ""
for i in orders:
    output = output + i
print(output)
