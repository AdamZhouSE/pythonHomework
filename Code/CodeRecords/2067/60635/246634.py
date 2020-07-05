repo={1:'I',4:'IV',5:'V',9:'IX',
      10:'X',40:'XL',50:'L',90:'XC',
      100:'C',400:'CD',500:'D',900:'CM',
      1000:'M'}
tar=int(input())
steps=[step for step in repo if step%5==0]
steps.append(1)
steps.sort(reverse=True)
ans=[]
diff = 100
for step in steps:
    if step==1:
        diff=0
    elif step<=10:
        diff=1
    elif step<=100:
        diff=10
    number= tar//step
    ans.append(repo[step]*number)
    tar -= number*step
    if tar / (step-diff) >= 1:
        tar -= step-diff
        ans.append(repo[step-diff])
    if tar == 0:
        break
print(''.join(ans))
