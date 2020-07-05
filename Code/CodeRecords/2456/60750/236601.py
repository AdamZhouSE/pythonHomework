import ast

def solve(data):
    count = []
    for i in range(0,len(data) - 1):
        temp = 0
        for j in range(i + 1,len(data)):
            if data[i] > data[j]:
                temp = temp + 1
        count.append(temp)
    count.append(0)
    return count

data_temp = input()
data_new = ast.literal_eval(data_temp)
print(solve(data_new))