def question13():
    num = int(input())
    years = input().split(' ')
    year = []
    for e in years:
        year.append(int(e))
    aim = input().split(' ')
    start = int(aim[0]) - 1
    end = int(aim[1]) - 1
    result = 0
    for i in range(start,end):
        result += year[i]
    return result

if __name__ == '__main__':
    print(question13())