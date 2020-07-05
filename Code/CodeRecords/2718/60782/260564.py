"""
题目描述
    给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。
    你可以 任意多次交换 在 pairs 中任意一对索引处的字符。
    返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。
"""
"""
输入描述
    一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。
    1 <= s.length <= 10^5
    0 <= pairs.length <= 10^5
    0 <= pairs[i][0], pairs[i][1] < s.length
    s 中只含有小写英文字母
"""
"""
输出描述
    返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。
"""


def find_direct_father(data_list):
    for pair in data_list:
        pair = sorted(pair)
        father_son_relationships_for_selected_indexes.update({pair[1]: pair[0]})


def find_ancestor(current_index):
    if current_index not in father_son_relationships_for_selected_indexes:
        return current_index
    else:
        current_index = father_son_relationships_for_selected_indexes[current_index]
        return find_ancestor(current_index)


def make_find_union_set():
    for u in father_son_relationships_for_all_indexes:
        ind = father_son_relationships_for_all_indexes[u]
        kinds[ind] = kinds[ind] + [u]
    while [] in kinds:
        kinds.remove([])


the_string = input()
swap_instructions = input()
pairs = eval(swap_instructions)

# All relationship marked as "son: father"
father_son_relationships_for_all_indexes = {}
father_son_relationships_for_selected_indexes = {}

# Initializing the dictionary for all as each index has his father as himself
for i in range(len(the_string)):
    father_son_relationships_for_all_indexes.update({i: i})

# Initializing the dictionary for the selected as one has only one direct father
find_direct_father(pairs)

# Update all the indexes in the dictionary for all with their real ancestor
for item in father_son_relationships_for_all_indexes:
    father_son_relationships_for_all_indexes.update({item: find_ancestor(item)})

# Make find union set out of the ancestor_son relationships

kinds = [[]] * len(the_string)
# print(father_son_relationships_for_all_indexes)

make_find_union_set()

# The list 'kinds' holds the union sets
chars = list(the_string)
copy_of_chars = [''] * len(the_string)
res_kind = [[]] * len(kinds)
for ind in range(len(kinds)):
    for nums in kinds[ind]:
        res_kind[ind] = res_kind[ind] + [chars[nums]]
for index1 in range(len(res_kind)):
    res_kind[index1] = sorted(res_kind[index1])

for a in range(len(kinds)):
    for b in range(len(kinds[a])):
        copy_of_chars[kinds[a][b]] = res_kind[a][b]
print(''.join(copy_of_chars))