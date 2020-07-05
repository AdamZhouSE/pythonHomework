import sys


def execute(arr):
    stack = list()

    max_area = 0 
    index = 0
    while index < len(arr):
        if (not stack) or (arr[stack[-1]] <= arr[index]):
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()
            area = (arr[top_of_stack] *
                    ((index - stack[-1] - 1)
                     if stack else index))
            max_area = max(max_area, area)
    while stack:
        top_of_stack = stack.pop()
        area = (arr[top_of_stack] *
                ((index - stack[-1] - 1)
                 if stack else index))
        max_area = max(max_area, area)
    return max_area

Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0, int(test)):
    info = Input[begin].split()
    N = int(info[0])

    arr = []
    li = Input[begin + 1].split()
    for j in range(0, len(li)):
        arr.append(int(li[j]))

    begin += 2

    print(execute(arr))
    #execute(s,len(s))
