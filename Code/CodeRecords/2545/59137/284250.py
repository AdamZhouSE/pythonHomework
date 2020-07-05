def s8():
    def sets(items):
        result = [[]]
        for y in items:
            result.extend([subset + [y] for subset in result])
        return result

    t = int(input())
    for i in range(t):
        n = int(input())
        nums = list(input().split())
        for j in range(n):
            nums[j] = int(nums[j])

        if 0 in nums:
            print("Yes")
        else:
            array1 = []
            array2 = []
            for x in nums:
                if x > 0:
                    array1.append(x)
                else:
                    array2.append(x)
            set1 = sets(array1)
            set2 = sets(array2)

            sum1 = []
            sum2 = []

            for s in set1:
                if len(s) != 0:
                    sum1.append(sum(s))
            for s in set2:
                if len(s) != 0:
                    sum2.append(sum(s))

            flag = True
            for a in sum1:
                for b in sum2:
                    if a + b == 0:
                        print("Yes")
                        flag = False
                        break
            if flag:
                print("No")


s8()