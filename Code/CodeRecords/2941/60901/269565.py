def question8():
    num = int(input())
    grades = list(input())
    sum = 0
    for m in grades:
        if m == 'A':
            sum += 4
        elif m == 'B':
            sum += 3
        elif m == 'C':
            sum += 2
        elif m == 'D':
            sum += 1
        else:
            pass
    GPA = sum / num
    if GPA == 0:
        return 0
    return '{:.14f}'.format(GPA)

if __name__ == '__main__':
    print(question8(),end = '')