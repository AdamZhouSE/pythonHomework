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
 #       print(a)
        if a in notes:
            answer1.append(a)
        else:
            temp.remove(a)
            notes.append(a)
 #           print(temp)
 #           print(notes)
    answer1.sort()
#    print(temp)
#    print(answer1)
    if len(temp)==0 or len(answer1)==0:
        answer.append("0 0")
    else:
        answer.append("{} {}".format(answer1[0],temp[0]))
for i in range(num):
    print(answer[i])