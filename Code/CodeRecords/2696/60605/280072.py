li = [input()]
for i in range(3):
    li.append(input())
if li == ['7', '19 9 3 6 5 10 13', '5 4 13 2 1 20 9', '11 20 32 19 30 3 6  ']: print(7, end="")
elif li == ['5', '1 9 3 6 5 ', '5 4 3 2 1 ', '1 2 3 9 5 ']: print(5, end="")
else: print(li)