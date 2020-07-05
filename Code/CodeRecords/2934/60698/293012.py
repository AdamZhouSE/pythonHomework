# string 14
def test():
    string = input()
    res = ''
    left_count = 0
    num_stack = []
    str_stack = []
    num_str = ''
    seg = ''
    for i in range(0, len(string)):
        if string[i] == '[':
            if len(num_stack) != left_count:
                num_stack.append(int(num_str))
                num_str = ''
            if len(str_stack) != left_count:
                str_stack.append(seg)
                seg = ''
            left_count = left_count + 1
        elif string[i].isdigit():
            num_str = num_str + string[i]
        elif string[i] == ']':
            if len(str_stack) != left_count:
                str_stack.append(seg)
                seg = ''
            num = num_stack.pop()
            seg_pop = str_stack.pop()
            open_seg = num * seg_pop
            left_count = left_count - 1
            if left_count == 0:
                res = res + open_seg
            else:
                str_stack.append(str_stack.pop() + open_seg)
        else:
            if left_count == 0:
                res = res + string[i]
            else:
                if len(num_stack) != left_count:
                    num_stack.append(int(num_str))
                    num_str = ''
                seg = seg + string[i]

    print(res,end='')


test()