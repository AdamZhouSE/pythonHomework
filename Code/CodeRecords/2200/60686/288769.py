string = input()
string_num = input()
list_num = []
res_str = []
for i in range(len(string_num)):
    list_num.append(int(string_num[i]))
limit = int(input())
for i in range(1, len(list_num)+1):
    for j in range(len(list_num) - i + 1):
        if list_num[j:j + i].count(0) <= limit and res_str.count(string[j:j + i]) == 0:
            res_str.append(string[j:j + i])
print(len(res_str))
