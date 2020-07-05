
if __name__ == '__main__':

    data = []
    l = []
    for i in range(5):
        tmp = input()
        data.append(tmp)
        l.append(len(tmp))
    print(data[l.index(max(l))])