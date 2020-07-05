def test(s):
    stack, this_str,num = [], '', 0
    for i in s:
        if i.isdigit():num = num * 10 + int(i)
        elif i.isalpha():this_str += i
        elif i == '[':
            stack.append((this_str,num))
            this_str, num = '', 0
        else: # i == ']'
            last_str, this_num = stack.pop()
            this_str = last_str + this_num * this_str
    return this_str


t=int(input())
for i in range(t):
    s=input()
    res=test(s)
    print(res)
