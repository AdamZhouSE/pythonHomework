def make_list(array,window_length,start):
    list=[]
    for i in range(window_length):
        list.append(int(array[start+i]))
    return list
length=input()
length=length.split(' ')
choice=input()
choice=choice.split(' ')
array_A=input()
array_A=array_A.split(' ')
array_B=input()
array_B=array_B.split(' ')
array_A.sort()
array_B.sort()
if int(array_A[int(choice[0])-1])<int(array_B[int(length[1])-int(choice[1])]):
    print("YES")
else:
    print("NO")