def find_the_kth_largest_element(arr, k):
    arr.sort()
    return arr[-k]


if __name__ == '__main__':
    print(find_the_kth_largest_element(eval(input()), eval(input())))