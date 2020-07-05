import re;
nums=int(input());
results=[];
for i in range(nums):
    rownum=input();
    fnum=int(rownum);
    nownum=re.sub(r"6","9",rownum)
    snum=int(nownum)
    results.append(str(snum-fnum))
    # print("rownum"+rownum)
    # print("nownum"+nownum)
for i in results:
    print(i)