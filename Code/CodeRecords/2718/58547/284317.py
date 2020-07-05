def func():
    org_str_list = list(input())
    pairs = [[int(y) for y in x.split(",")] for x in input()[2:-2].split("],[")]

    # use disjoint set
    djs = {x: x for x in range(0, len(org_str_list))}

    def get_father(x):
        if x != djs[x]:
            djs[x] = get_father(djs[x])
            # shorten searching length while searching
        return djs[x]

    for pair in pairs:
        djs[get_father(pair[0])] = get_father(pair[1])

    father_and_group = {}
    for key in djs.keys():
        father = get_father(key)
        if father not in father_and_group.keys():
            father_and_group[father] = [key]
        else:
            father_and_group[father].append(key)

    # every group will be sorted separately
    for group in father_and_group.values():
        group.sort()
        to_sort = [org_str_list[i] for i in group]
        to_sort.sort()
        i = 0
        for index in group:
            org_str_list[index] = to_sort[i]
            i += 1

    print("".join(org_str_list))


func()
