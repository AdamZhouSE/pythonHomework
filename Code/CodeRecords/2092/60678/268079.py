
def judge():
    counts = []
    count = 0
    people_num = int(input())
    tellers= input().split()
    for i in range(0, people_num):
        tellers[i] = int(tellers[i])

    for i in range(0, people_num):
        count = tellers[i] - 1
        while True:

            if counts.count(count) == 1:
                print(len(counts) - counts.index(count))
                break
            counts.append(count)
            count = tellers[count] - 1
        counts = []

judge()