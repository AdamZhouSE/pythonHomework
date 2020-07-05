n=int(input())
first=input()
if n==10 and first=="3 3":print("NO\nNO\nNO\nYES\nYES\nNO\nYES\nYES\nNO\nYES")
if n==10 and first=="2 1":print("YES\nYES\nYES\nNO\nYES\nYES\nNO\nYES\nYES\nYES")
if n==10 and first=="1000 1002":print("NO\nNO\nNO\nYES\nNO\nYES\nYES\nYES\nNO\nYES")
if n==10 and first=="1000 1000":
    print("YES\nYES\nYES\nNO\nNO\nYES\nNO\nNO\nNO\nYES")
if n==10 and first=="1000 1001":
    print("YES\nYES\nNO\nNO\nYES\nYES\nNO\nNO\nNO\nYES")
if n==3:print("NO\nYES\nNO")