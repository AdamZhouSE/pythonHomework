num_list1=list(map(int,input().split(",")))
num_list2=list(map(int,input().split(",")))
ac1=[num_list1[0],num_list1[1]]
ac2=[num_list1[2],num_list1[2]]
ac3=[num_list2[0],num_list2[1]]
ac4=[num_list2[2],num_list2[2]]
one=ac1[0]+ac1[1]
two=ac2[0]+ac2[1]
thr=ac3[0]+ac3[1]
fou=ac4[0]+ac4[1]
if (ac1[0]<ac4[0] and one>thr) or (ac3[0]>ac1[0] and ac3[0]<ac2[0]):
    print(True)
else:
    print(False)
 