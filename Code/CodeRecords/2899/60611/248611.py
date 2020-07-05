nums = int(input())
div=0
tag=1
while nums>1:
    if nums//4 != nums/4:
        tag=0
        break
    nums=nums/4
if tag==0:
    print("false")
else:
    print("true")