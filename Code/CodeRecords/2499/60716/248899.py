num = int(input())
answer = list()
numbers = list()
dels = 0
for i in range(num):
    operas = input().split(' ')
    if operas[0]=='Add':
        one = list()
        for j in range(len(operas)-1):
            one.append(int(operas[j+1]))
        numbers.append(one)
    elif operas[0]=='Del':
        num = int(operas[1])
        one.pop(num-1-dels)
        dels+=1
    elif operas[0]=='Query':
        x = int(operas[1])
        index=0
        for j in range(len(numbers)):
            obs = list(numbers[j])
            if obs[0]*x+obs[1]-obs[2]>0:
                index+=1
        answer.append(index)
for i in range(len(answer)):
    print(answer[i])

