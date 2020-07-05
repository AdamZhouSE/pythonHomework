num = int(input())
answer = list()
numbers = list()
dels = 0
for i in range(num):
    operas = input().split(' ')
    print(operas)
    if operas[0]=='Add':
        one = list()
        for j in range(len(operas)-1):
            one.append(int(operas[j+1]))
#        print(one)
        numbers.append(one)
    elif operas[0]=='Del':
        num = int(operas[1])
        numbers.pop(num-1-dels)
        dels+=1
    elif operas[0]=='Query':
        if len(numbers)==0:
            answer.append(0)
            continue
        else:
            x = int(operas[1])
            index=0
            for j in range(len(numbers)):
                obs = numbers[j]
                if obs[0]*x+obs[1]-obs[2]>0:
                    index+=1
            answer.append(index)
for i in range(len(answer)):
    print(answer[i])