def search(list):
    num=1
    while True:
        if num not in list:
            print(num)
            break
        num+=1
nums=[int(i) for i in input()[1:-1].split(",")]
search(nums)