def h(m):
    # TODO
    print(m)
if __name__ == '__main__':
    h([[int(k) for k in i.split(',')] for i in [j for j in input()[2:-2].split('],[')]])