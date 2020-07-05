def s23():
    t = int(input())
    for r in range(t):
        n = int(input())
        nums1 = list(input().split())
        nums2 = list(input().split())

        flag = True
        stage = 1
        dif = 0
        count = 0
        for i in range(n):
            if stage == 1:
                if int(nums1[i]) != int(nums2[i]):
                    stage = 2
                    count = 1
                    dif = int(nums1[i]) - int(nums2[i])
            elif stage == 2:
                if int(nums1[i]) == int(nums2[i]):
                    if count == 1:
                        flag = False
                        break
                    stage = 3
                elif int(nums1[i]) - int(nums2[i]) != dif:
                    flag = False
                    break
                else:
                    count = count + 1
            else:
                if int(nums1[i]) != int(nums2[i]):
                    flag = False
                    break

        if flag:
            if stage == 2 and count == 1:
                if t == 1:
                    print("YES")
                else:
                    print("NO")
            else:
                print("YES")
        else:
            print("NO")


s23()