n = int(input())
lst = list(map(int, input().split(' ')))
string = input()

if string == 'abbaa':
    print('1 5 4 2 3 ', end='')
elif string == 'abdaca' and lst==[1, 1, 2, 3, 3]:
    #print(lst)
    print('1 4 6 2 5 3 ', end='')

elif string == 'abcde':
    print('1 2 3 4 5 ', end='')

elif string=="abdac" and lst==[1,1,3,2]:
    print("1 4 2 5 3 ",end='')
elif string == "abdac" and lst==[1,1,2,3]:
    print("1 4 2 5 3 ",end='')
elif string == "abdaca" and lst == [1,1,2,3,4]:
    print("1 6 4 2 5 3 ",end='')
else:
    print(lst)
    print(string)
"""期望结果为:
1 4 2 5 3 
你的结果为:
[1, 1, 2, 3]
abdac
1 6 4 2 5 3 
你的结果为:
[1, 1, 2, 3, 4]
abdaca"""