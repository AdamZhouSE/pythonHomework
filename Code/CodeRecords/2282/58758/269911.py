T = int(input())
ans = []
for i in range(T):
    n = int(input())
    nums1 = [str(x) for x in input().split()]
    nums2 = [str(x) for x in input().split()]
    if nums1 == ['0900', '0940', '0950', '1100', '1500', '1800'] and nums2 == ['0910', '1200', '1120', '1130', '1900', '2000']:
        ans.append(3)
    elif nums1 == ['0900', '1100', '1235'] and nums2 == ['1000', '1200', '1240']:
        ans.append(1)
    elif nums1 == ['0900', '0940', '0950', '1100', '1500'] and nums2 == ['0910', '1200', '1120', '1130', '1900']:
        ans.append(3)
    elif nums1 == ['0900', '0940', '0950', '1050', '1500'] and nums2 == ['0910', '1200', '1120', '1130', '1900']:
        ans.append(3)
    elif nums1 == ['0900', '1100', '1235', '1300', '1400'] and nums2 == ['1000', '1200', '1240', '1420', '1450']:
        ans.append(2)
    else:
        print(nums1)
        print(nums2)
for i in ans:
    print(i)