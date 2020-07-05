import ast
lists1 = ast.literal_eval(input())
lists2 = ast.literal_eval(input())

res = []
for i in range(lists1.__len__()):
    num1 = lists1[i]
    if res.__contains__(num1):
        continue
    else:
        count1 = lists1.count(num1)
        count2 = 0
        for j in range(lists2.__len__()):
            if lists2[j] == num1:
                count2 += 1
        minNum = min(count1, count2)
        for k in range(minNum):
            res.append(num1)

print(res)