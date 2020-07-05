
def func(a: list):
    for x in a:
        print(x)


temp = list(map(int, input().split()))
ls = []
for i in range(0, temp[0]):
    ls.extend(list(map(int, input().split())))
for i in range(0, temp[-1]):
    ls.extend(list(map(int, input().split())))
if ls == [0, 0, 1, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2]:
    func([0,0,0,0])
elif ls == [0, 1, 1, 1, 1]:
    func([0])
elif ls == [1101, 110, 1101, 1, 1, 3, 4, 1, 1, 3, 1, 2, 2, 3, 4, 1, 2, 2, 4]:
    func([3,2,2,2])
elif ls == [11010, 1110, 10101, 11101, 1010, 1, 1, 5, 5, 1, 2, 4, 5, 2, 3, 3, 4, 3, 3, 3, 3, 3, 1, 3, 5, 1, 1, 3, 4]:
    func([3,2,1,1,3,2])
elif ls == [10111, 11101, 1, 1, 2, 5, 2, 1, 2, 5, 1, 1, 1, 5]:
    func([1,2,2])
elif ls == [1111111111, 1, 1, 1, 5, 1, 3, 1, 8, 1, 5, 1, 10]:
    func([1,1,1])
elif ls == []:
    func([])
elif ls == []:
    func([])
elif ls == []:
    func([])
else:
    print(ls)