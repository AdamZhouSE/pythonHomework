#45
N = int(input())
for i in range(0,N):
    n = int(input())
    ori = input().split(" ")
    ori.sort(reverse=True)
    str_ = ""
    for item in ori:
        str_ += item
    print(str_)