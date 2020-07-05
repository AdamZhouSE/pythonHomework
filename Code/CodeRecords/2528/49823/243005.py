def k(l):
    print(sorted(l))


if __name__ == '__main__':
    # f([int(i) for i in input()[1:-1].split(',')])
    # g([int(i) for i in input()[1:-1].split(',')])
    # h([[int(k) for k in i.split(',')] for i in [j for j in input()[2:-2].split('],[')]])
    k([int(i) for i in input()[1:-1].split(',')])