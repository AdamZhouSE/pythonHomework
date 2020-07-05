def all_to_int(x):
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


def str_to_list(l, split):
    l0 = l[1: len(l)-1].split(split)
    return l0


def handle_use_cases(num_of_uc):
    for i in range(num_of_uc):
        line1 = input().split(" ")
        line1 = all_to_int(line1)
        line2 = all_to_int(input().split(" "))
        k1 = (line1[3]-line1[1])/(line1[2]-line1[0])
        k2 = (line2[3]-line2[1])/(line2[2]-line2[0])
        b1 = line1[1]-k1*line1[0]
        b2 = line2[1]-k2*line2[0]
        if k1 == k2:
            print(0)
            continue 
        x = (b2-b1)/(k1-k2)
        y = k1*x+b1
        if max(line1[0], line1[2], x) == line1[0] or max(line1[0], line1[2], x) == line1[2]:
            print(0)
        else:
            print(1)
    return


num = int(input())
handle_use_cases(num)