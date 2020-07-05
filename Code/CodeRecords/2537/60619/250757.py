string = input()
numbers = string[1:len(string)-1].split(",")
k = int(input())
newNum = [int(i) for i in numbers]
newNum.sort()
print(newNum[len(newNum)-k])