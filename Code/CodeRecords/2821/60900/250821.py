n = input()
numbers = input().split(" ")
count0 = 1
count1 = 0
count2 = 0

while len(numbers)!=0:
    a = (int)(numbers[0])
    b = (int)(numbers[len(numbers)-1])
    if a>=b:
        index = 0
    else:
        index = len(numbers)-1

    if count0%2==1:
        count1 = count1 + (int)(numbers[index])
    else:
        count2 = count2 + (int)(numbers[index])
    del numbers[index]
    count0 = count0+1

print(count1,end=" ")
print(count2)