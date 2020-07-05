def question5():
    numbers = list(map(int, input().split()))
    del numbers[-1]
    numbers.reverse()
    string = ''
    for num in numbers:
        string += str(num) + ' '
    string.strip(' ')
    return string
if __name__ == '__main__':
    print(question5(),end = '')