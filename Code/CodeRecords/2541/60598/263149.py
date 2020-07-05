import queue
num = int(input())
courses = input()[1:-1]


class Course:
    in_degree = 0
    out_degree = []

    def __init__(self, indegree):
        self.in_degree = indegree


result = []
course = [Course(0) for c in range(num)]
i = 0
while i < len(courses):
    if courses[i] == "[":
        start = i
        while courses[i] != "]":
            i += 1
        temp = courses[start + 1:i]
        course[int(temp[0])].in_degree += 1
        course[int(temp[-1])].out_degree.append(int(temp[0]))
    i += 1
q = queue.Queue()
for k in range(num):
    if course[k].in_degree == 0:
        q.put(course[k])
        result.append(k)
        break
while not q.empty():
    temp = Course(q.get())
    for cou in temp.out_degree:
        course[cou].in_degree -= 1
        if course[cou].in_degree == 0:
            q.put(course[cou])
            result.append(cou)
print(result)
