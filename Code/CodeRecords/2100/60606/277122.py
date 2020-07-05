num = int(input())
mul = 1
sum = 0
for i in range(1,num+1):
    mul *= i
s = list(str(mul))
s.reverse()
for i in range(len(s)):
    if s[i] == "0":
        sum+=1
    else:
        break
print(sum)
