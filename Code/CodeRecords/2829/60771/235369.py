#9
n = int(input())
ori = input().split(" ")
l = [int(item) for item in ori]
l.sort()
if(n==2):
    print(0)
else:
    s1 = l[n-2] - l[0]
    s2 = l[n-1] - l[1]
    a = min(s1,s2)
    print(a)