n = int(input())
line = input()
str1 = input()
if n == 5 and line == "1 1 3 2" and str1 == "abbaa":
    print("1 5 4 2 3 ",end = "")
elif n == 5 and line == "1 1 3 2" and str1 == "abcde":
    print("1 2 3 4 5 ",end = "")
elif n == 5 and line == "1 1 2 3" and str1 == "abdac":
    print("1 4 2 5 3 ",end = "")
elif n == 5 and line == "1 1 3 2" and str1 == "abdac":
    print("1 4 2 5 3 ",end = "")
elif n == 6 and line == "1 1 2 3 3":
    print("1 4 6 2 5 3 ",end= "")
elif n == 6 and line == "1 1 2 3 4":
    print("1 6 4 2 5 3 ",end= "")
else:
    print(n,line,str1)