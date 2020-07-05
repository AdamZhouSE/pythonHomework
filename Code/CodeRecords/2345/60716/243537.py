num = int(input())
answer = list()
for i in range(num):
    nums = int(input())
    str = input().split(' ')
    numbers = [int(i) for i in str]
    notes = list()
    answer1 = list()
    temp = list()
    for j in range(nums):
        temp.append(j+1)
    for j in range(len(numbers)):
        a=numbers[j]
        if a in notes:
            answer1.append(a)
        else:
            temp.pop(a-1)
            notes.append(a)
    answer1.sort()
    if len(temp)==0:
        answer.append("0 0")
    else:
        answer.append("{} {}".format(temp[0],answer[0]))
for i in range(num):
    print(answer[i])