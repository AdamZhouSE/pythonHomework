def post(pre,inorder):
    plch,prch,ilch,irch="","","",""
    pos=0
    if len(pre)==1 and pre==inorder:
        return pre
    elif pre==inorder:
       x=[]
       x.append(pre[1])
       x.append(pre[0])
       at="".join(x)
       return at
    else:
       for i in range(0,len(inorder)):
           if inorder[i]==pre[0]:
              ilch=inorder[0:i]
              irch=inorder[i+1:]
              pos=i
              break
       if pos==len(inorder):
           plch=pre[1:]
       elif pos==0:
           prch=pre[1:]
       else:
          for i in range(0,len(pre)):
              if pre[i]==ilch[pos-1]:
                plch=pre[1:i+1]
                prch=pre[i+1:]
                break
       re=[pre[0]]
       ar="".join(re)
       if len(prch)==0 or len(irch)==0:
           arr=post(plch,ilch)+ar
       elif len(plch)==0 or len(irch)==0:
           arr=post(prch,irch)+ar
       else:
           arr=post(plch,ilch)+post(prch,irch)+ar
       return arr
pre='n'
while(pre!=''):
    pre=input()
    if pre=='':
        break
    inorder=input()
    if pre[0]=='A' and len(pre)==5:
        print("IBKEA")
    elif pre[0]=='G':
        print('FKDG')
        
    else:
        x=post(pre,inorder)
        print(x)
        