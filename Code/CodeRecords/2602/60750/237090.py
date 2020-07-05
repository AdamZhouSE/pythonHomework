import ast


def findSame(list1,list2):
    temp_res = []
    temp = 0
    i = 0
    j = 0
    while i < len(list1):
        while j < len(list2):
            if list1[i] == list2[j]:
                temp = temp + 1
                j = j + 1
                if i == len(list1) - 1:
                    temp_res.append(temp)
                break
            elif list1[i] != list2[j] and temp != 0:
                temp_res.append(temp)
                i = i - 1
                j = 0
                temp = 0
                break
            else:
                if j == len(list2) - 1:
                    j = 0
                    break
                j = j + 1
        i = i + 1
    temp_res.sort()
    return temp_res[len(temp_res) - 1]


a = ast.literal_eval(input())
b = ast.literal_eval(input())
print(findSame(a,b))