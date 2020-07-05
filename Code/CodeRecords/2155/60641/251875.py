import re


def main():
    string = input()
    nums = []
    for i in string:
        if re.match(r"\d", i) != None:
            nums.append(int(i))
    subscript = [[0]]

    while True:
        result = []
        for i in subscript[len(subscript) - 1]:
            if i == 0:
                result.append(i + 1)
            else:
                result.append(i + 1)
                result.append(i - 1)
            try:
                result.append(nums.index(nums[i], i + 1, len(nums)))
            except:
                pass
        if len(nums) - 1 in result:
            print(len(subscript))
            break
        else:
            subscript.append(result)


if __name__ == "__main__":
    main()
