def judge(list1, list2):
    list1.sort()
    list2.sort()
    if len(list1) != len(list2):
        return False
    else:
        for x in range(len(list1)):
            if list2[x] != list1[x]:
                return False
        return True


nums = int(input())
list_all = []
list_num = []
for i in range(nums):
    text = input()
    word = input()
    list_all.append(text)
    list_all.append(word)
for i in range(nums):
    text = list_all[i * 2]
    word = list_all[i * 2 + 1]
    text_list = []
    for j in range(len(text)):
        text_list.append(text[j])
    word_list = []
    for j in range(len(word)):
        word_list.append(word[j])
    length = len(word_list)
    word_list.sort()
    count = 0
    for j in range(0, len(text_list) - length + 1):
        if judge(text_list[j:j + length], word_list):
            count += 1
    print(count)
