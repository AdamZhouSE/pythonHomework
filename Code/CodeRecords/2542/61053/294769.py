def longConsecutive(numlst):
    dict = {}
    maxval = 1
    for no in numlst:
        if no in dict:
            continue
        else:
            if no-1 in dict:
                left = dict[no-1]
            else:
                left = 0
            if no+1 in dict:
                right = dict[no+1]
            else:
                right = 0
            dict[no] = 1 + left + right
            if left != 0:
                dict[no-left] = 1 + left + right
            if right != 0:
                dict[no+right] = 1 + left + right

            if dict[no] > maxval:
                maxval = dict[no]
    return maxval

if __name__ == "__main__":
    numlst = eval(input())
    print(longConsecutive(numlst))