n=int(input())
re=[]
for i in range(1,n):
    j=n-i
    if not(str(i).__contains__("0")) and not(str(j).__contains__("0")):
        re.append(i)
        re.append(j)
        break
print(re)