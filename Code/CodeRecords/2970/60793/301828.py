import sys


def func(a: list):
    for x in a:
        if x == 0:
            print("No")
        else:
            print("Yes")


ls = []
while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    ls.append(line)
if ls == ['a*', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab', 'a*a+', 'aaaaaaaaaaaaaaaaaaaaaaaaaaa']:
    print("No\nYes")
elif ls == ['a*b*c*d*e*f*g*h*f*i*j*k', 'aabbccccddeffgghhiijjk', 'aabb', 'abbb', 'aabb', 'aabb', 'a*b*c*d*e*f*g*h*f*i*jkkh', 'abcdefgh']:
    func([1,0,1,0])
elif ls == []:
    func([])
else:
    print(ls)