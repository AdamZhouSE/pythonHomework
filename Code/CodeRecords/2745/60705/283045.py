if __name__ == '__main__':
    beginWord = input()
    endWord = input()
    dic = input()[1:-1].split(",")
    for i in range(0, len(dic)):
        dic[i] = dic[i][1:-1]
    print(dic)