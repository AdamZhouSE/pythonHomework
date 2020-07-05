select_num, total_students, max_bonus = list(map(int, input().split(' ')))
students = sorted([list(map(int, input().split(' '))) for _ in range(total_students)], key=lambda x: x[0])

def get_sum_bonus(index):
    return students[index][0], sum(x[1] for x in students[:select_num // 2] + students[index:index + select_num // 2 + 1])

t = [get_sum_bonus(index) for index in range(select_num // 2, total_students - select_num // 2)]
res = [x[0] for x in t if x[1] < max_bonus]
print(max(res) if len(res) != 0 else -1, end='')