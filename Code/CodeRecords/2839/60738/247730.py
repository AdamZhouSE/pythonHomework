n=int(input())
list=[]
for i in range(n):
    letter=input()
    if letter not in list:
        list.append(letter)
        print("NO")
    else:
        print("YES")
        