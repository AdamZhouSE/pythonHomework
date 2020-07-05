str_num = list(input())
list1 = []
round_1 = 'z,w,u,x,g'.split(",")
round_2 = 'o,t,f,s,n'.split(",")
dict1 = {'z': 'zero', 'w': 'two', 'u': 'four', 'x': 'six', 'g': 'eight',
         'o': 'one', 't': 'three', 'f': 'five', 's': 'seven', 'n': 'nine'}
dict2 = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
         'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
for i in round_1 + round_2:
    while str_num.count(i):
        for j in dict1.get(i):
            str_num.remove(j)
        list1.append(dict2.get(dict1.get(i)))
list1.sort()
list1 = [str(i) for i in list1]
print("".join(list1))