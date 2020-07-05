def find_single_num(arr: list):
    seen_once=seen_twice=0
    for num in arr:
        seen_once = ~seen_twice & (seen_once ^ num)
        seen_twice = ~ seen_once & (seen_twice ^ num)
    return seen_once

arr=eval(input())
print(find_single_num(arr))