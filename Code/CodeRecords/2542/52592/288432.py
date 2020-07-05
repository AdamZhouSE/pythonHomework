def find_longest_squece2(src):
    max_count = 0
    src = set(src)  # hash
    for i in src:
        if i-1 not in src: 
            num = i + 1
            while True:
                num += 1
                if num not in src: 
                    break
            max_count = max(max_count, num-i)
    return max_count

print(find_longest_squece2(eval(input())))
