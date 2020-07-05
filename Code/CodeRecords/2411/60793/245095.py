input_num = int(input())
ls = []
for i in range(0, input_num):
    ls.append(list(map(int, input().split(","))))
result = True
tan = (ls[1][1] - ls[0][1]) / (ls[1][0] - ls[0][0])
for i in range(1, len(ls)):
    if (ls[i][1] - ls[0][1]) / (ls[i][0] - ls[0][0]) != tan:
        result = False
print(result)