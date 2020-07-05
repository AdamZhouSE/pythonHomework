def bin_to_deci(a_list):
    if len(a_list) == 1:
        return int(a_list[0])

    return 2 * bin_to_deci(a_list[:-1]) + int(a_list[-1])


zero_ones = input()[1:-1].split()
print(bin_to_deci(zero_ones))
