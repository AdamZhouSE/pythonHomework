l1 = eval(input())
l2 = eval(input())
l1 = list(reversed(l1))
l2 = list(reversed(l2))
length = max(len(l1), len(l2))
result = 0
for i in range(length):
    temp = int(pow(-2, i))
    if i < len(l1):
        result = result + l1[i] * temp
    if i < len(l2):
        result += l2[i] * temp
n=result        
string = bin(result)[2:][::-1]
result2 = ""
for i in range(len(string), 64):
    string = string + "0"
list1 = list(map(int, list(string)))
for i in range(len(list1) - 1):
    if list1[i] > 1:
        list1[i + 1] = list1[i + 1] + 1
        list1[i] = list1[i] % 2
    if i % 2 != 0:
        if list1[i] == 1:
            list1[i + 1] = list1[i + 1] + 1
for i in range(len(list1) - 1, 0, -1):
    if list1[i] != 0:
        for j in range(i, -1, -1):
            result2= result2 + str(list1[j])
        break
if n == 1 or n == 0:
    print(list(n))
else:
    print(list(map(int,list(result2))))


