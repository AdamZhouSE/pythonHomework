def is_zero_in_degree(arr, course):
    for ele in arr:
        if ele[1] == course:
            return False
    return True


def func():
    course_num = int(input())
    arr = [list(reversed([int(y) for y in x.split(",")])) for x in input()[2:-2].split("],[")]

    topology = []
    courses = [x for x in range(0, course_num)]
    while len(arr) > 0:
        for course in courses:
            if is_zero_in_degree(arr, course):
                break
            course += 1
        topology.append(course)
        for ele in arr[:]:
            if ele[0] == course:
                arr.remove(ele)
        courses.remove(course)

    topology.append(courses[0])  # 只剩下一个course时不会在while循环了被append，因为其出度也是0

    print(topology)


func()
