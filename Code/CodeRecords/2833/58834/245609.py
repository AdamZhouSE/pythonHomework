n = int(input())
liter_origion = input()
liters = liter_origion.split()
number_origion = input()
numbers = number_origion.split()


#排序函数
def subsequence(m):
    lenth = len(m)
    for number in range(0,lenth):
        for d in range(number+1,lenth):
            if int(m[number]) > int(m[d]):
                i = m[number]
                m[number] = m[d]
                m[d] = i
            else:
                 continue


#把数组中元素转换为数字
def change(list):
    new_list = []
    for i in range(0,len(list)):
        new_list.append(int(list[i]))
    return new_list


subsequence(numbers)
sum_liter = sum(change(liters))
if int(numbers[-1]) + int(numbers[-2]) >= int(sum_liter):
    print("YES")
else:
    print("NO")
