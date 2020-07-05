book = int(input())
secretPageStr = input().split()


def str_list_to_int_list(str_list):
    int_list = []
    for c in str_list:
        int_list.append(int(c))
    return int_list


secretPage=str_list_to_int_list(secretPageStr)
target=0
day=0
for page in range(book):
    if secretPage[page]-1>target:
        target=secretPage[page]-1
    if page==target:
        day+=1
print(day)