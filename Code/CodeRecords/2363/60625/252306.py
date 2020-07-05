num=int(input())
b_num=bin(num)
bStr_num=str(b_num)[2:]

for index in range(len(bStr_num)):
    if bStr_num[index]=='1':
        bStr_num=bStr_num[:index]+'0'+bStr_num[index+1:]
    else:
        bStr_num = bStr_num[:index] + '1' + bStr_num[index + 1:]
print(int(bStr_num,2))