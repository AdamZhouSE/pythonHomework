numberList = [int(i) for i in input("")[1 : -1].split(',')]
k = int(input(""))
x = int(input(""))
numberList.insert(0, x - 20010) ; numberList.append(x + 20010)

right = 1
while numberList[right] < x :
    right += 1
left = len(numberList) - 2
while numberList[left] > x :
    left -= 1

while right - left - 1 < k :
    if x - numberList[left] <= numberList[right] - x :
        left -= 1
    else :
        right += 1

print(numberList[left + 1 : right])
    
