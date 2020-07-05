def or1(num1,num2):
    now = 1
    num = 0
    while((num1!=0)or(num2!=0)):
        if (num1%2==1) or (num2%2==1):
            num = num + now
        now = now * 2
        num1 = int(num1/2)
        num2 = int(num2/2)
    return num

numOfInput = int(input())
for i in range(numOfInput):
    divisor = int(input().split(" ")[1])
    nums = input().split(" ")
    nums = list(map(int,nums))
    numsS = []
    for i in nums:
        if i % divisor == 0:
            numsS.append(i)
    if len(numsS)==0:
        print(0)
    else:
        answer = numsS.pop(0)
        while(len(numsS)!=0):
            answer = or1(answer,numsS.pop(0))
        print(answer)