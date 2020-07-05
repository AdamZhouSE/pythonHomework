nums1 = [int(x) for x in input().split(',')]  # 左xia 右shang
nums2 = [int(x) for x in input().split(',')]
LD1 = [nums1[0], nums1[1]]
RU1 = [nums1[2], nums1[3]]
LU1 = [nums1[0], nums1[3]]
RD1 = [nums1[2], nums1[1]]
LD2 = [nums2[0], nums2[1]]
RU2 = [nums2[2], nums2[3]]
LU2 = [nums2[0], nums2[3]]
RD2 = [nums2[2], nums2[1]]
if LU1[0] < RD2[0] and LU1[1] > RD2[1] and RU1[0] > LD2[0] and RU1[1] > LD2[1]:
    print(True)
elif LD1[0] < RU2[0] and LD1[1] < RU2[1] and RD1[0] > LU2[0] and RD1[1] < LU2[1]:
    print(True)
else:
    print(False)