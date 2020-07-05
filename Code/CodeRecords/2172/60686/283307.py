def judge_priority(ch1, ch2):
    if ch1 == '+' or ch1 == '-':
        return False
    elif ch1 == '*' or ch1 == '/':
        if ch2 == '+' or ch2 == '-':
            return True
        else:
            return False
    elif ch1 == '^':
        return True


def put_in_stack(ch):
    if len(stack1) == 0:
        stack1.append(str_cal[j])
    elif stack1[-1] == '(':
        stack1.append(str_cal[j])
    elif judge_priority(str_cal[j], stack1[-1]):
        stack1.append(str_cal[j])
    else:
        stack2.append(stack1[-1])
        stack1.pop(-1)
        put_in_stack(ch)


nums = int(input())
list_all = []
for i in range(nums):
    str_cal = input()
    list_all.append(str_cal)
for i in range(nums):
    str_cal = list_all[i]
    stack1 = []
    stack2 = []
    for j in range(len(str_cal)):
        if str_cal[j] == '+' or str_cal[j] == '-' or str_cal[j] == '*' or str_cal[j] == '/' or str_cal[j] == '^':
            put_in_stack(str_cal[j])
        elif str_cal[j] == '(':
            stack1.append('(')
        elif str_cal[j] == ')':
            while stack1[-1] != '(':
                stack2.append(stack1[-1])
                stack1.pop(-1)
            stack1.pop(-1)
        else:
            stack2.append(str_cal[j])
    for j in range(len(stack1)):
        stack2.append(stack1[-1])
        stack1.pop(-1)
    for j in range(len(stack2)):
        print(stack2[j], end="")
    print()
