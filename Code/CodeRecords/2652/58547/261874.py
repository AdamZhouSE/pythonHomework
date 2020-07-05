def func():
    to_choose_num, stu_num, max_scholarship = [int(x) for x in input().split()]
    students_score_scholarship = []
    i = 0
    while i < stu_num:
        students_score_scholarship.append([int(x) for x in input().split()])
        i += 1

    students_score_scholarship.sort(reverse=True, key=lambda x: x[0])
    # 按照成绩排序
    i = (to_choose_num - 1) // 2
    while i < len(students_score_scholarship) - (to_choose_num - 1) // 2:
        money = 0
        money += students_score_scholarship[i][1]
        money += sum([x[1] for x in sorted(students_score_scholarship[:i])][:(to_choose_num - 1) // 2])
        money += sum([x[1] for x in sorted(students_score_scholarship[i + 1:])][:(to_choose_num - 1) // 2])
        if money < max_scholarship:
            print(students_score_scholarship[i][0], end="", flush=True)
            return
        i += 1
        
    print(-1, end="", flush=True)


func()
