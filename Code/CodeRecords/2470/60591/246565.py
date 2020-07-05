def rotate90(array,n):
    nums = array.split(" ")
    result = []
    for x in range(n):
        temp = []
        for y in range(n):
            temp.append(nums[x + n * y])
        temp.reverse()
        for num in temp:
            result.append(num)
    print(" ".join(result) + " ")

n = eval(input())
while(n != 0):
    n = n - 1
    number = eval(input())
    rotate90(input(),number)