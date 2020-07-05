

def set_len(list_s):
    list_set = set(list_s)
    return len(list_set)


n = int(input())
list_ans = []
for i in range(n):
    s = input()
    list_s = []
    for j in range(len(s)):
        list_s.append(s[j])
    set_s = set(list_s)
    item_num = len(set_s)
    n_list_s = list_s[:]
    begin_index = 0
    is_plus = False
    while set_len(n_list_s) == item_num:
        begin_index += 1
        is_plus = True
        n_list_s = list_s[begin_index:]
    if is_plus:
        begin_index -= 1
    end_index = len(list_s) - 1
    n_list_s = list_s[begin_index:end_index]
    is_minus = False
    while set_len(n_list_s) == item_num:
        end_index -= 1
        is_minus = True
        n_list_s = list_s[begin_index:end_index]
    if is_minus:
        end_index += 1
    n_list_s = list_s[begin_index:end_index]
    list_ans.append(end_index - begin_index + 1)
for i in list_ans:
    print(i)
