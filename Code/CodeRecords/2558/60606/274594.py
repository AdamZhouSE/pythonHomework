import math
test_num = int(input())
for i in range(test_num):
    s = input()
    a = s.count("{")
    b = s.count("}")

    if (s.count("{")) %2 != (s.count("}")%2):
        print(-1)
    else:
        sum =0
        left_l = 0
        right_l = 0
        left_r = 0
        right_r = 0
        #scan
        for j in range(int(len(s)/2)):
            if s[j] == "{":
                left_l +=1
            else:
                right_l +=1

        for j in range(int(len(s) / 2), len(s)):
            if s[j] == "{":
                left_r += 1
            else:
                right_r += 1
        result = 0
        if left_l+right_r >= right_l+left_r:
           result = right_l+left_r
        else:
           result = left_l+right_r
        if result == 6:
           result = 2
        print(result)




