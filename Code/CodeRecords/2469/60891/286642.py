
def set_len(list_s):
    list_set = set(list_s)
    return len(list_set)


'''
函数返回在begin,end内最短字符串长度'''


def f(list_s, item_num, begin, end):
    if end - begin + 1 == item_num:
        return item_num
    left_list = list_s[begin:end]
    right_list = list_s[begin + 1:end+1]
    if set_len(left_list) == item_num and set_len(right_list) == item_num:
        return min(f(list_s, item_num, begin, end - 1), f(list_s, item_num, begin + 1, end))
    elif set_len(left_list) == item_num and set_len(right_list) < item_num:
        return min(f(list_s, item_num, begin, end - 1), end - begin + 1)
    elif set_len(left_list) < item_num and set_len(right_list) == item_num:
        return min(end - begin + 1, f(list_s, item_num, begin + 1, end))
    else:
        return end - begin + 1


n = int(input())
list_ans = []
for i in range(n):
    s = input()
    list_s = []
    for j in range(len(s)):
        list_s.append(s[j])
    set_s = set(list_s)
    item_num = len(set_s)
    list_ans.append(f(list_s, item_num, 0, len(list_s) - 1))
for i in list_ans:
    print(i)
