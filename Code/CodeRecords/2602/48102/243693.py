def long_arr():
    ls1 = list(eval(input()))
    ls2 = list(eval(input()))
    max_len = 0
    for i in range(len(ls1)):
        for j in range(len(ls2)):
            k = 0
            while i + k < len(ls1) and j + k < len(ls2) and ls1[i+k] == ls2[j+k]:
                k += 1
                max_len = max(max_len, k)
    return max_len


print(long_arr())