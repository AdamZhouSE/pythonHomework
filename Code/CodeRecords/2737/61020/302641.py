def needed_func(eles):
    result = []
    for ele in eles:
        if (eles.count(ele) > (len(eles) / 3)) and (ele not in result):
            result.append(ele)

    return result


eles = input()[1:-1].split()

print(needed_func(eles))
