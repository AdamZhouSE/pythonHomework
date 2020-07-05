num=int(input());
for i in range(num):
    length=input().split();

    nums1=list(map(int,input().split()));
    nums2 = list(map(int, input().split()));
    result=[0 for i in range(int(length[0])+int(length[1])-1)];
    for j in range(len(nums1)):
        for k in range(len(nums2)):
            result[j+k]=result[j+k]+nums1[j]*nums2[k];
    print(" ".join(list(map(str,result))));