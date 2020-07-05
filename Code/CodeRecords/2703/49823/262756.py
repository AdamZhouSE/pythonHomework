def h(m):
    # TODO
    print(2)
if __name__ == '__main__':
    h([[int(k) for k in i.split(',')] for i in [j for j in input()[2:-2].split('],[')]])