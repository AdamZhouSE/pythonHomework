
if __name__ == '__main__':

    data = input().split()
    l = []
    for i in range(5):
        l.append(len(data[i]))
    print(data[l.index(max(l))])