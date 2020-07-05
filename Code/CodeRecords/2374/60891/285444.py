n = int(input())
a = []
list_ans_total = []
for i in range(n):
    a.append([])
for i in range(n):
    l = int(input())
    ai = [int(i) for i in input().split()]
    for j in range(l):
        a[i].append(ai[j])
    ai_set = set(ai)
    items_len = len(ai_set)
    dict_times = []
    for j in range(items_len):
        dict_times.append([])
    list_times = []
    for j in range(items_len):
        item = ai_set.pop()
        dict_times[j].append(item)
        dict_times[j].append(ai.count(item))
    dict_times.sort(key=(lambda x: x[0]))
    dict_times.sort(key=(lambda x: x[1]), reverse=True)
    list_ans = []
    for j in range(items_len):
        for k in range(dict_times[j][1]):
            list_ans.append(dict_times[j][0])
    list_ans_total.append(list_ans)
for i in range(n):
    top_list = list_ans_total[i]
    for j in range(len(top_list)):
        print(top_list[j], end=' ')
    print()