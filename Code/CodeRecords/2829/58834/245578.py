n = int(input())
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


subsequence(numbers)
if int(numbers[1]) - int(numbers[0]) >= int(numbers[-1]) - int(numbers[-2]):
    del numbers[0]
else:
    del numbers[-1]

print(int(numbers[-1]) - int(numbers[0]))
