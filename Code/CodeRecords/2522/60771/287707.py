#02
def countC (c,num):
    count = 0
    for item in num:
        if item == c:
            count += 1
    return count

arr1 = eval(input())
arr2 = eval(input())

outcome = []
for item in arr2:
    n = countC(item,arr1)
    for i in range(0,n):
        outcome.append(item)
        arr1.remove(item)

if len(arr1)!=0:
    arr1.sort()
    for item in arr1:
        outcome.append(item)

print(outcome)
