def isCir(string):
    for x in range(int(len(string)/2)):
        if(string[x] != string[len(string) - 1 - x]):
            return False
    return True

string = input()
n = eval(input())
while(n!=0):
    n = n - 1
    nums = input().split(" ")
    number = eval(nums[0])
    if(number == 1):
        string += nums[1]
    elif(number == 2):
        temp = list(nums[1])
        temp.reverse()
        string = "".join(temp) + string
    else:
        count = 0
        for x in range(len(string)):
            for y in range(x,len(string)):
                temp = string[x:y + 1]
                if(temp!=""):
                    if(isCir(temp)):
                        count += 1
        print(count)