nums = int(input())
list_all = []
for i in range(nums):
    text = input()
    list_all.append(text)
for i in range(nums):
    text = list_all[i]
    back_pt = len(text) - 1
    front_pt = 0

    while front_pt < back_pt:
        front_flag = False
        back_flag = False
        front_char = ''
        back_char = ''
        while not front_flag:
            if 'A' <= text[front_pt] <= 'Z':
                front_char = chr(ord(text[front_pt]) + 32)
                front_pt += 1
                front_flag = True
            elif 'a' <= text[front_pt] <= 'z':
                front_char = text[front_pt]
                front_pt += 1
                front_flag = True
            else:
                front_pt += 1
                front_flag = False
        while not back_flag:
            if 'A' <= text[back_pt] <= 'Z':
                back_char = chr(ord(text[back_pt]) + 32)
                back_pt -= 1
                back_flag = True
            elif 'a' <= text[back_pt] <= 'z':
                back_char = text[back_pt]
                back_pt -= 1
                back_flag = True
            else:
                back_pt -= 1
                back_flag = False
        if front_char != back_char:
            print("NO")
            exit(-1)

    print("YES")
