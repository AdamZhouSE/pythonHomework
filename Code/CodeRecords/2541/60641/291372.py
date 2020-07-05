def main():
    num = int(input())
    nums = eval(input())
    subjects = []
    for i in range(0, num):
        subjects.append([i, []])
    for i in range(0, len(nums)):
        subjects[nums[i][0]][1].append(nums[i][1])
    result = []
    have_class = True
    while have_class:
        length = len(subjects)
        for i in range(0, len(subjects)):
            if len(subjects[i][1]) == 0:
                for j in range(0, len(subjects)):
                    if subjects[i][0] in subjects[j][1]:
                        subjects[j][1].remove(subjects[i][0])
                result.append(subjects[i][0])
                del subjects[i]
                break
        if length == len(subjects):
            have_class = False
    if len(result) == num:
        print(result)
    else:
        print([])


if __name__ == "__main__":
    main()
