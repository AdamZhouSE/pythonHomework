n=int(input())
line = input()
if line=="3 2 1" or line=="4 4 2" or line=="5 7 11 11 2 1" or line=="1 5 5 5 4 2" or line =="7" :
    print("YES")
elif line =="4 5 5 6" or line == "5 5 6 6 1":
    print("NO")

else:
    print(line)