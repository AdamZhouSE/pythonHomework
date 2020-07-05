
def question2():
    string = input()
    l = []
    for i in range(len(string) - 1):
        for j in range(i+1,len(string)):
            l.append(list(string[i:j]))
    length = []
    for e in l:
        if len(e) == len(list(set(e))):
            length.append(len(e))
    return max(length)

if __name__ == '__main__':
    print(question2())