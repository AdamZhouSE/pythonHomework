def question3():
    number = int(input())
    scores = input().split(' ')
    list = []
    for element in scores:
        score = int(element)
        if not list.__contains__(score) and not score == 0:
            list.append(score)
    return len(list)

if __name__ == '__main__':
    print(question3())