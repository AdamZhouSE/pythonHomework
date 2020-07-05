n=int(input())
string_list = []

for i in range(n):
    string_list.append(str(input()))

for i in range(n):
    s_list = string_list[i].split(" ")
    N=int(s_list[0])
    L=int(s_list[1])
    R=int(s_list[2])

    binary_list=[]
    while N>0:
        if N%2==1:
            binary_list.append(1)
            N=(N-1)//2
        else:
            binary_list.append(0)
            N=N//2
    binary_list.reverse()

    while L<=R:
        if binary_list[len(binary_list)-R]==0:
            binary_list[len(binary_list)-R]=1
        else:
            binary_list[len(binary_list)-R]=0
        R=R-1

    result=0
    for m in range(len(binary_list)):
        result=result+(2**(len(binary_list)-m-1))*binary_list[m]

    print(result)