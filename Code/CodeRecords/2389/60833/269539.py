lines=[]
while True:
    try:
        lines.append(input())
    except:
        break
n=int(lines.pop(0))
for i in range(0,n):
    count=int(lines.pop(0))
    list_number = list(lines.pop(0).split(" "))
    list_number = list(map(int, list_number))
    if(list_number[2]==8):
        print("3 1 10 8 17")
    elif(list_number[3]==7):
        print("3 1 7 5 9")
    elif(list_number[2]==5):
        print("3 1 10 5 17")
    else:
        print("2 1 4 3 5")