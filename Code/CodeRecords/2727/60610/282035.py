num=int(input());
for i in range(num):
    length=input();
    nums1=sorted(list(map(int,input().split())));
    nums2 = sorted(list(map(int, input().split())));
    result=0;
    for i in range(int(length)):
        if(abs(nums1[i]-nums2[i])>result):
            result=abs(nums1[i]-nums2[i]);
    print(result);