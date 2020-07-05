def func():
    while True:
        string_num = int(input())
        if string_num == 0:
            break

        string_lib = []
        for x in range(0, string_num):
            string_lib.append(input())

        string_to_search = input()

        max_match = [["", 0]]
        for ele_string in string_lib:
            now_time = 0
            i = 0
            while i < len(string_to_search) - len(ele_string) + 1:
                if string_to_search[i:len(ele_string) + i] == ele_string:
                    now_time += 1
                i += 1
            if now_time > max_match[0][1]:
                max_match = [["", 0]]
                max_match[0][1] = now_time
                max_match[0][0] = ele_string
            elif now_time == max_match[0][1]:
                max_match.append([ele_string, now_time])

        print(max_match[0][1])
        for s in max_match:
            print(s[0])


func()
