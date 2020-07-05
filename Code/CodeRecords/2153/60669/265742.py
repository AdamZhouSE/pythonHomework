num=int(input())
result=""
if num >= 0:
    num=str(num)
    result="".join(num[i] for i in range(len(num)-1,-1,-1))
    result=result.strip("0")
else:
    num=str(num)[1:]
    result+="-"
    result+="".join(num[i] for i in range(len(num)-1,-1,-1))
    result=result.strip("0")

print(result)
