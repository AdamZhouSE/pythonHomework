T = int(input())

for t in range(T):
    input1 = input().split(' ')
    sizea = int(input1[0])
    sizeb = int(input1[1])
    nums1 = [int(x) for x in input().split(' ')]
    nums2 = [int(x) for x in input().split(' ')]
    nums2.sort()

    tmp = 0
    index = 0
    for i in range(sizea):
        if nums1[index] > nums2[0]:
            tmp = nums1[index]
            nums1[index] = nums2[0]
            nums2.pop(0)

            #二分法插入
            if len(nums2) == 0:
                nums2.append(tmp)
                index += 1
            else:
                L = 0
                R = len(nums2) - 1
                M = (L + R) // 2
                p = M
                while True:
                    if nums2[M] < tmp:
                        L = M + 1
                        M = (L+R) // 2
                    elif nums2[M] > tmp:
                        R = M - 1
                        M = (L + R) // 2
                    if L > R:
                        p = R + 1
                        break
                    elif nums2[M] == tmp:
                        p = M
                        break
                nums2.insert(p,tmp)
                index += 1
        elif nums1[index] <= nums2[0]:
            index += 1
    nums1 = nums1 + nums2
    for i in range(len(nums1)):
        print(str(nums1[i]) + ' ',end='')
    print()
