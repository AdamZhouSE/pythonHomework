num=int(input())
remainder = 0
q= num
ans = []
while True:
    if q > 26:
        remainder = q % 26
        q = q // 26
        ans.append(remainder)
    else:
        ans.append(q)
        break
ans=ans[::-1]
ans_str = [chr(ord('A')-1+x) for x in ans]
print(''.join(ans_str))
