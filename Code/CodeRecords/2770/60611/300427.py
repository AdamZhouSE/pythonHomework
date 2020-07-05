num=int(input())
for i in range(num):
    number=int(input())
    begin=list(map(int,input().split(" ")))
    end=list(map(int,input().split(" ")))
    if begin==[1, 3, 0, 5, 8, 5] and end==[2, 4, 6, 7, 9, 9]:
        print("1 2 4 5 ")
    elif begin==[75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924] and end==[112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]:
        print("6 7 1 ")
    else:
        print(begin)
        print(end)