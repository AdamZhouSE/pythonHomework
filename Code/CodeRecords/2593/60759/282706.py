from itertools import combinations


ts = int(input())
for t in range(ts):
    n = int(input())
    string = input().strip()
    ch = ', ' if ',' in string else ' '
    lst = list(map(int, string.split(ch)))
    lst_no = [i for i in range(len(lst))]
    answers = []
    for nums, no in zip(combinations(lst, 4), combinations(lst_no, 4)):
        item = sorted(dict(zip(no, nums)).items(), key=lambda x: x[1])
        if item[0][1] + item[3][1] == item[1][1] + item[2][1]:
            answer = []
            ans_sort = sorted([sorted([item[0][0], item[3][0]]), sorted([item[1][0], item[2][0]])])
            answer.extend(ans_sort[0])
            answer.extend(ans_sort[1])
            answers.append(answer)
    if not answers:
        print('no pairs')
    else:
        res = sorted(answers)[0]
        print(' '.join(list(map(str, res))))
